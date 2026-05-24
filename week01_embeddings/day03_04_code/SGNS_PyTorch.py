import torch
import torch.nn as nn
import torch.nn.functional as F

class SkipGramNegativeSampling(nn.Module):
    def __init__(self, vocab_size, embed_dim):
        super(SkipGramNegativeSampling, self).__init__()
        
        # 1. The "Two Vectors" Nuance
        # v_c: Matrix for center words
        self.center_embeddings = nn.Embedding(vocab_size, embed_dim)
        # u_o: Matrix for context words
        self.context_embeddings = nn.Embedding(vocab_size, embed_dim)
        
        # Initialize weights randomly, but keep them small
        init_range = 0.5 / embed_dim
        self.center_embeddings.weight.data.uniform_(-init_range, init_range)
        self.context_embeddings.weight.data.uniform_(-init_range, init_range)

    def forward(self, center_words, positive_contexts, negative_contexts):
        """
        center_words: Tensor of shape [batch_size]
        positive_contexts: Tensor of shape [batch_size]
        negative_contexts: Tensor of shape [batch_size, K]
        """
        # --- Positive Pass ---
        # Get v_c and u_o
        v_c = self.center_embeddings(center_words)           # [batch_size, embed_dim]
        u_o = self.context_embeddings(positive_contexts)     # [batch_size, embed_dim]
        
        # Compute dot product: u_o^T * v_c
        # We use element-wise multiplication and sum across the embedding dimension
        pos_dot = torch.sum(v_c * u_o, dim=1)                # [batch_size]
        
        # Log-Sigmoid for the positive pairs: log(sigma(u_o^T * v_c))
        pos_loss = F.logsigmoid(pos_dot)                     # [batch_size]
        
        # --- Negative Pass ---
        # Get u_n for the K negative samples
        u_n = self.context_embeddings(negative_contexts)     # [batch_size, K, embed_dim]
        
        # Compute dot product: u_n^T * v_c
        # Reshape v_c to use batch matrix multiplication (bmm) against the K noise words
        v_c_reshaped = v_c.unsqueeze(2)                      # [batch_size, embed_dim, 1]
        neg_dot = torch.bmm(u_n, v_c_reshaped).squeeze(2)    # [batch_size, K]
        
        # Log-Sigmoid for the negative pairs: log(sigma(-u_n^T * v_c))
        # Notice the negative sign applied to neg_dot!
        neg_loss = torch.sum(F.logsigmoid(-neg_dot), dim=1)  # [batch_size]
        
        # --- Total Objective ---
        # We want to MAXIMIZE the above terms, which means MINIMIZING their negative sum.
        total_loss = -(pos_loss + neg_loss).mean()
        
        return total_loss

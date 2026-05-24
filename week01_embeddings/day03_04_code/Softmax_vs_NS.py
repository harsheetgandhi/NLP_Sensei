import torch
import time

# --- Setup Parameters ---
vocab_size = 50000   # Standard vocabulary size
embed_dim = 300      # Standard embedding dimensions
batch_size = 512     # Number of center words processed at once
K = 5                # Number of negative samples

print(f"Benchmarking Batch Size: {batch_size} | Vocab: {vocab_size} | Dim: {embed_dim}\n")

# --- 1. Softmax Approach ---
# We need the vectors for our 512 center words
center_embeddings = torch.randn(batch_size, embed_dim)
# We also need the matrix for the ENTIRE 50,000 word vocabulary
vocab_embeddings = torch.randn(vocab_size, embed_dim)

start_softmax = time.perf_counter()

# To get the denominator, we must multiply the center words against EVERY word in the vocab
softmax_logits = torch.matmul(center_embeddings, vocab_embeddings.T) # Shape: [512, 50000]
# Then compute the exponentials and sum them up
softmax_denom = torch.exp(softmax_logits).sum(dim=1)                 # Shape: [512]

time_softmax = time.perf_counter() - start_softmax


# --- 2. Negative Sampling (SGNS) Approach ---
# We only need the vectors for the 1 True Context word...
positive_embeddings = torch.randn(batch_size, embed_dim)
# ...and the K (5) randomly sampled noise words
negative_embeddings = torch.randn(batch_size, K, embed_dim)

start_ns = time.perf_counter()

# Calculate dot product for just the positive pair
pos_dot = torch.sum(center_embeddings * positive_embeddings, dim=1)  # Shape: [512]

# Calculate dot product for just the K negative pairs
# .unsqueeze() is used to align the matrix dimensions for batch multiplication
center_reshaped = center_embeddings.unsqueeze(2)
neg_dot = torch.bmm(negative_embeddings, center_reshaped).squeeze(2) # Shape: [512, 5]

time_ns = time.perf_counter() - start_ns


# --- Results ---
print(f"Softmax Time:          {time_softmax:.5f} seconds")
print(f"Negative Sample Time:  {time_ns:.5f} seconds")
print("-" * 40)
print(f"Negative Sampling is roughly {time_softmax / time_ns:.0f}x faster!")
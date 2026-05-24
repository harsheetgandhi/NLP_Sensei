import torch
import time

# --- Setup Parameters ---
vocab_size = 50000   
embed_dim = 300      
batch_size = 512     
K = 5                

print(f"Benchmarking Batch Size: {batch_size} | Vocab: {vocab_size} | Dim: {embed_dim}\n")

# ==========================================
# 1. Negative Sampling (SGNS) Approach
# ==========================================
center_embeddings = torch.randn(batch_size, embed_dim)
positive_embeddings = torch.randn(batch_size, embed_dim)
# K negative samples for each word in the batch
negative_embeddings = torch.randn(batch_size, K, embed_dim)

start_ns = time.perf_counter()

# Calculate dot product for just the positive pair
pos_dot = torch.sum(center_embeddings * positive_embeddings, dim=1)  

# Calculate dot product for just the K negative pairs
center_reshaped = center_embeddings.unsqueeze(2)
neg_dot = torch.bmm(negative_embeddings, center_reshaped).squeeze(2) 

time_ns = time.perf_counter() - start_ns


# ==========================================
# 2. GloVe Approach
# ==========================================
# GloVe only uses the center word and context word. It does NOT need negative 
# samples because the 0-counts are already handled during the matrix creation!
glove_center = torch.randn(batch_size, embed_dim)
glove_context = torch.randn(batch_size, embed_dim)

# GloVe also uses scalar bias terms for both words
bias_center = torch.randn(batch_size)
bias_context = torch.randn(batch_size)

# We mock the pre-calculated log(N) target from the global matrix
log_co_occurrences = torch.randn(batch_size) 
# We mock the weighting function f(N)
f_n_weights = torch.rand(batch_size)

start_glove = time.perf_counter()

# 1. Dot product of center and context
glove_dot = torch.sum(glove_center * glove_context, dim=1)

# 2. Add biases and subtract the target log(N)
diff = glove_dot + bias_center + bias_context - log_co_occurrences

# 3. Square the difference and multiply by the weighting function f(N)
glove_loss = torch.sum(f_n_weights * (diff ** 2))

time_glove = time.perf_counter() - start_glove


# --- Results ---
print(f"Negative Sample Time:  {time_ns:.5f} seconds")
print(f"GloVe Time:            {time_glove:.5f} seconds")
print("-" * 40)

if time_glove < time_ns:
    print(f"GloVe's training step is roughly {time_ns / time_glove:.1f}x faster than SGNS!")
else:
    print("Execution times are roughly equivalent at this batch size.")

"""

Negative Sample Time:  0.06056 seconds
GloVe Time:            0.02385 seconds
----------------------------------------
GloVe's training step is roughly 2.5x faster than SGNS!
"""
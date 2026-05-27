import numpy as np
from scipy.linalg import orthogonal_procrustes
from scipy.spatial.distance import cosine

# 1. The Alignment Function (Your snippet)
def align_spaces(embeddings_1920, embeddings_2020):
    """
    Aligns the 1920s embedding space to the 2020s embedding space.
    Assumes rows in both matrices correspond to the exact same vocabulary words.
    """
    # orthogonal_procrustes finds the best rotation matrix (W) to align them
    W, scale = orthogonal_procrustes(embeddings_1920, embeddings_2020)
    
    # Rotate the 1920s space to match the 2020s space
    aligned_1920 = np.dot(embeddings_1920, W)
    
    return aligned_1920

# 2. Setup Mock Data
print("--- Simulating Semantic Spaces ---")
vocab = ["apple", "car", "gay", "telephone", "mouse", "iphone", "macbook", "ipod","rodent","laptop","device"]
vocab_size = len(vocab)
embed_dim = 100 # Standard 100-dimensional embeddings

# Create random embeddings for 1920s and 2020s
np.random.seed(42)
embeddings_1920 = np.random.randn(vocab_size, embed_dim)
embeddings_2020 = np.random.randn(vocab_size, embed_dim)

# Let's artificially make the word "gay" (index 2) highly DIFFERENT in the 2020s
# while keeping a word like "apple" (index 0) relatively similar.
embeddings_2020[0] = embeddings_1920[0] + np.random.normal(0, 0.1, embed_dim) # Small change
embeddings_2020[2] = np.random.randn(embed_dim) * 5                           # Massive change

# 3. Align the Spaces
print("Aligning 1920s space to 2020s space using Orthogonal Procrustes...")
aligned_1920 = align_spaces(embeddings_1920, embeddings_2020)

# 4. Measure Semantic Change
print("\n--- Measuring Semantic Change ---")
target_words = ["apple", "gay"]

for word in target_words:
    word_index = vocab.index(word)
    
    # Get the aligned 1920s vector and the 2020s vector
    vec_1920_aligned = aligned_1920[word_index]
    vec_2020 = embeddings_2020[word_index]
    
    # Calculate Cosine Distance (0 means identical, 2 means completely opposite)
    # Cosine Distance = 1 - Cosine Similarity
    distance = cosine(vec_1920_aligned, vec_2020)
    
    print(f"Word: '{word}'")
    print(f"Cosine Distance: {distance:.4f}")
    if distance > 0.8:
        print(" -> Conclusion: MASSIVE SEMANTIC CHANGE DETECTED.\n")
    else:
        print(" -> Conclusion: Meaning remained relatively stable.\n")
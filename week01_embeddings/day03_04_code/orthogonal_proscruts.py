import numpy as np
from scipy.linalg import orthogonal_procrustes
from scipy.spatial.distance import cosine

# 1. Mock Data: A tiny vocabulary of 3 words in 2 dimensions
vocab = ["apple", "car", "gay"]

# 2020s Space (Target)
space_2020 = np.array([
    [2.0, 3.0],   # apple
    [-2.0, 4.0],  # car
    [3.0, -1.0]   # gay (Modern context)
])

# 1920s Space (Source) 
# Imagine this space is naturally rotated by 30 degrees during training.
# Also, the word "gay" had a completely different meaning (e.g., happy/joyful), 
# so its internal position relative to "apple" and "car" is totally different.
space_1920 = np.array([
    [-0.7, 3.5],  # apple (rotated)
    [-4.2, 1.4],  # car (rotated)
    [-2.0, -3.0]  # gay (Different meaning + rotated)
])

# 2. Apply Orthogonal Procrustes
# W is the optimal rotation matrix
W, scale = orthogonal_procrustes(space_1920, space_2020)

# 3. Rotate the 1920s space using W
aligned_1920 = np.dot(space_1920, W)

# 4. Measure Semantic Change (Cosine Distance)
print("--- Semantic Change Detection ---")
for i, word in enumerate(vocab):
    # Compare the newly aligned 1920 vector to the 2020 vector
    dist = cosine(aligned_1920[i], space_2020[i])
    print(f"Word: '{word}' | Distance: {dist:.4f}")
    
    if dist > 0.5:
        print("  -> MASSIVE SEMANTIC CHANGE DETECTED.\n")
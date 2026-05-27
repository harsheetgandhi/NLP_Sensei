import gensim.downloader as api
import warnings
warnings.filterwarnings('ignore') # Ignore gensim deprecation warnings for clean output

print("Loading pre-trained GloVe vectors (this may take a minute)...")
# We'll load a 100-dimensional GloVe model trained on Wikipedia
model = api.load("glove-wiki-gigaword-100")
print("Model loaded successfully!\n")

# ==========================================
# 1. NEAREST NEIGHBORS (The "Frog" Example)
# ==========================================
print("--- 1. Nearest Neighbors ---")
target_word = "frog"
print(f"What is mathematically closest to '{target_word}'?")

# most_similar computes the cosine similarity between 'frog' and the entire vocabulary
neighbors = model.most_similar(target_word, topn=5)
for word, score in neighbors:
    print(f"  -> {word} (Similarity: {score:.3f})")


# ==========================================
# 2. WORD SIMILARITY BENCHMARKING
# ==========================================
print("\n--- 2. Word Similarity ---")
word1, word2 = "money", "bank"
word3, word4 = "money", "refrigerator"

# .similarity calculates the exact Cosine Similarity between two specific vectors
sim_high = model.similarity(word1, word2)
sim_low = model.similarity(word3, word4)

print(f"Similarity between '{word1}' & '{word2}': {sim_high:.3f}")
print(f"Similarity between '{word3}' & '{word4}': {sim_low:.3f}")


# ==========================================
# 3. LINEAR STRUCTURES (Vector Math / Analogies)
# ==========================================
print("\n--- 3. Vector Math & Analogies ---")

# Equation 1: King - Man + Woman = ?
# In gensim, 'positive' adds vectors together, 'negative' subtracts them.
print("Equation: King - Man + Woman = ?")
analogy_1 = model.most_similar(positive=['king', 'woman'], negative=['man'], topn=1)
print(f"  Result: {analogy_1[0][0]} (Confidence: {analogy_1[0][1]:.3f})")

# Equation 2: Paris - France + Germany = ? (Geography)
print("\nEquation: Paris - France + Germany = ?")
analogy_2 = model.most_similar(positive=['paris', 'germany'], negative=['france'], topn=1)
print(f"  Result: {analogy_2[0][0]} (Confidence: {analogy_2[0][1]:.3f})")

# Equation 3: Walking - Walk + Swim = ? (Syntax/Grammar)
print("\nEquation: Walking - Walk + Swim = ?")
analogy_3 = model.most_similar(positive=['walking', 'swim'], negative=['walk'], topn=1)
print(f"  Result: {analogy_3[0][0]} (Confidence: {analogy_3[0][1]:.3f})")

"""
Loading pre-trained GloVe vectors (this may take a minute)...
Model loaded successfully!

--- 1. Nearest Neighbors ---
What is mathematically closest to 'frog'?
  -> toad (Similarity: 0.701)
  -> snake (Similarity: 0.657)
  -> frogs (Similarity: 0.629)
  -> monkey (Similarity: 0.621)
  -> turtle (Similarity: 0.610)

--- 2. Word Similarity ---
Similarity between 'money' & 'bank': 0.572
Similarity between 'money' & 'refrigerator': 0.159

--- 3. Vector Math & Analogies ---
Equation: King - Man + Woman = ?
  Result: queen (Confidence: 0.770)

Equation: Paris - France + Germany = ?
  Result: berlin (Confidence: 0.885)

Equation: Walking - Walk + Swim = ?
  Result: swimming (Confidence: 0.801)
"""
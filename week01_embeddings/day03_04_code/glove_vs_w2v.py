from gensim import downloader as api
from gensim.models import Word2Vec
import time

print("Loading the 'text8' corpus (a slice of Wikipedia)...")
# text8 is a real-world corpus of about 17 million words
corpus = api.load('text8') 

# ==========================================
# 1. Train Word2Vec (Negative Sampling) from Scratch
# ==========================================
print("\n--- Training Word2Vec (Skip-Gram with Negative Sampling) ---")
start_w2v = time.perf_counter()

# sg=1 means Skip-Gram, negative=5 means 5 noise words, window=5 is our context
w2v_model = Word2Vec(corpus, vector_size=100, window=5, sg=1, negative=5, min_count=5, workers=4)

time_w2v = time.perf_counter() - start_w2v
print(f"Word2Vec Training Time: {time_w2v:.2f} seconds")

# Test the Context!
print("\nWord2Vec's understanding of 'cat':")
w2v_results = w2v_model.wv.most_similar('cat', topn=5)
for word, score in w2v_results:
    print(f"  - {word} (Similarity: {score:.3f})")


# ==========================================
# 2. Load Pre-trained GloVe Vectors
# ==========================================
print("\n--- Loading Pre-Trained GloVe Vectors ---")
# We download pre-trained GloVe vectors (trained on 6 Billion words from Wikipedia)
# Loading this takes a minute, but training it from scratch would take days!
start_glove = time.perf_counter()

glove_model = api.load('glove-wiki-gigaword-100')

time_glove = time.perf_counter() - start_glove
print(f"GloVe Loading Time: {time_glove:.2f} seconds")

# Test the Context!
print("\nGloVe's understanding of 'cat':")
glove_results = glove_model.most_similar('cat', topn=5)
for word, score in glove_results:
    print(f"  - {word} (Similarity: {score:.3f})")

"""
--- Training Word2Vec (Skip-Gram with Negative Sampling) ---
Word2Vec Training Time: 395.37 seconds

Word2Vec's understanding of 'cat':
  - prionailurus (Similarity: 0.687)
  - felis (Similarity: 0.685)
  - albino (Similarity: 0.684)
  - guppy (Similarity: 0.683)
  - dog (Similarity: 0.682)

--- Loading Pre-Trained GloVe Vectors ---
GloVe Loading Time: 63.84 seconds

GloVe's understanding of 'cat':
  - dog (Similarity: 0.880)
  - rabbit (Similarity: 0.742)
  - cats (Similarity: 0.732)
  - monkey (Similarity: 0.729)
  - pet (Similarity: 0.719)
"""

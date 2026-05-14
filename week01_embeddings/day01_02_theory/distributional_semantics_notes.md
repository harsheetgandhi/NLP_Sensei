# Day 1: Word Embeddings & Distributional Semantics

## 1. Distributional Semantics: The "Firth" Philosophy
The core idea behind word embeddings is the **Distributional Hypothesis**: 
> "You shall know a word by the company it keeps." — J.R. Firth (1957)

Instead of sparse One-Hot Encoded vectors, we want **dense vectors** (e.g., 300 dimensions) where mathematically similar vectors represent semantically similar words.

## 2. Word2Vec: CBOW vs. Skip-gram
* **CBOW (Continuous Bag of Words):** Predicts the target word based on surrounding context words.
* **Skip-gram:** Predicts the surrounding context words given a single target word. (Better for rare words).

## 3. The Math: Skip-gram Objective Function
Word2Vec iterates through the corpus with a sliding window. At position $t$, for a central word $w_t$ and window size $m$, we want to maximize the probability of context words.

**Loss Function (Negative Log-Likelihood):**
$$J(\theta) = -\frac{1}{T} \sum_{t=1}^T \sum_{-m \le j \le m, j \ne 0} \log P(w_{t+j} | w_t ; \theta)$$

**The Softmax Probability:**
$$P(o|c) = \frac{\exp(u_o^\top v_c)}{\sum_{w \in V} \exp(u_w^\top v_c)}$$
* $u_o^\top v_c$: Dot product similarity between center word and context word.
* The denominator forces the model to calculate similarity against the *entire vocabulary*, which is why we use **Negative Sampling** in practice.

## 4. Hyperparameters
* **Window Size ($m$):** Small windows (2-5) capture *syntactic* similarity (e.g., words that function similarly in grammar). Large windows (5-15+) capture *topical* similarity.
* **Learning Rate & Epochs:** Standard gradient descent parameters.

---
### 💡 Business Intuition (Data Science Application)
In a supply chain or e-commerce context, Word2Vec can map unstructured text. For example, product descriptions for "sneakers" and "running shoes" will end up grouped together in the vector space, allowing for robust search, recommendation systems, or resolving synonymous logistics terms automatically without hardcoding rules.

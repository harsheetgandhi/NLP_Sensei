"""
1. Advanced Count-Based Methods (The HAL Model)
Simple co-occurrence matrices treat all words in a window equally. 
But intuitively, a word immediately next to the center word carries more syntactic meaning than a word 5 spaces away. 
Furthermore, English is highly directional: what comes before a word is functionally different than what comes after it.
How HAL (Hyperspace Analogue to Language) fixes this:
Distance Weighting: 
    Instead of adding $+1$ for every co-occurrence, HAL adds a weight inversely proportional to the distance. 
    If the window size is 5, a word at distance 1 gets a score of 5, distance 2 gets 4, etc.
Left/Right Separation:
    Instead of a $|V| \times |V|$ matrix, HAL creates a $|V| \times 2|V|$ matrix. 
The word "cute" appearing to the left of "cat" is recorded in a completely different column than if it appeared to the right.
"""

import numpy as np

def build_hal_matrix(tokens, vocab_size, window_size=5):
    # Matrix shape: Vocab Size x (2 * Vocab Size) for Left and Right contexts
    hal_matrix = np.zeros((vocab_size, 2 * vocab_size))
    
    for i, target_word_id in enumerate(tokens):
        # Look left and right within the window
        for dist in range(1, window_size + 1):
            weight = window_size - dist + 1  # Closer words get higher weights
            
            # Left Context
            if i - dist >= 0:
                left_word_id = tokens[i - dist]
                hal_matrix[target_word_id, left_word_id] += weight
                
            # Right Context (Offset by vocab_size)
            if i + dist < len(tokens):
                right_word_id = tokens[i + dist]
                hal_matrix[target_word_id, right_word_id + vocab_size] += weight
                
    return hal_matrix

# Example Usage:
if __name__ == "__main__":
    # Sample tokenized corpus (word IDs)
    tokens = [0, 1, 2, 3, 4, 5]  # Example token IDs
    vocab_size = 6  # Assume we have 6 unique words in our vocab
    
    hal_matrix = build_hal_matrix(tokens, vocab_size)
    print("HAL Matrix Shape:", hal_matrix.shape)
    print("HAL Matrix:\n", hal_matrix)  

"""
HAL Matrix:
 [[0. 0. 0. 0. 0. 0. 0. 5. 4. 3. 2. 1.]
 [5. 0. 0. 0. 0. 0. 0. 0. 5. 4. 3. 2.]
 [4. 5. 0. 0. 0. 0. 0. 0. 0. 5. 4. 3.]
 [3. 4. 5. 0. 0. 0. 0. 0. 0. 0. 5. 4.]
 [2. 3. 4. 5. 0. 0. 0. 0. 0. 0. 0. 5.]
 [1. 2. 3. 4. 5. 0. 0. 0. 0. 0. 0. 0.]]
"""
import random

def get_dynamic_context(tokens, current_index, max_window_size):
    # Randomly sample the window size for this specific step!
    dynamic_window = random.randint(1, max_window_size)
    
    start = max(0, current_index - dynamic_window)
    end = min(len(tokens), current_index + dynamic_window + 1)
    
    context_words = tokens[start:current_index] + tokens[current_index+1:end]
    return context_words
# Example Usage:
if __name__ == "__main__":
    # Sample tokenized corpus (word IDs)
    tokens = [0, 1, 2, 3, 4, 5]  # Example token IDs
    max_window_size = 3
    
    for i in range(len(tokens)):
        context = get_dynamic_context(tokens, i, max_window_size)
        print(f"Target Word ID: {tokens[i]}, Context Word IDs: {context}")
"""
Target Word ID: 0, Context Word IDs: [1]
Target Word ID: 1, Context Word IDs: [0, 2]
Target Word ID: 2, Context Word IDs: [0, 1, 3, 4]
Target Word ID: 3, Context Word IDs: [1, 2, 4, 5]
Target Word ID: 4, Context Word IDs: [3, 5]
Target Word ID: 5, Context Word IDs: [2, 3, 4]
"""
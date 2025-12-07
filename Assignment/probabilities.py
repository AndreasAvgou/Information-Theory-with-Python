def calculate_probabilities(freq_data):
    """
    Calculates the probability of appearance for each letter.
    Input: Dictionary {letter: frequency}
    Output: Dictionary {letter: probability}
    """
    total_count = sum(freq_data.values())
    probabilities = {}
    
    # Calculate probability for each letter (frequency / total_count)
    for letter, count in freq_data.items():
        probabilities[letter] = count / total_count
        
    return probabilities
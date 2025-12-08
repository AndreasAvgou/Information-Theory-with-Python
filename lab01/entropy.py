import math

def calculate_entropy(probabilities):
    """
    Calculates the Shannon Entropy given a list of probabilities.
    Formula: H = - sum(p * log2(p))
    
    Args:
        probabilities (list): List of probability values.
    Returns:
        float: Entropy in bits.
    """
    entropy = 0.0
    for p in probabilities:
        if p > 0:
            entropy -= p * math.log2(p)
    return entropy
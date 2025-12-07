import math

def calculate_entropy(probabilities):
    """
    Calculates the Shannon Entropy of the source.
    Formula: H = - sum(P(i) * log2(P(i)))
    """
    entropy = 0.0
    for p in probabilities.values():
        if p > 0:
            entropy += p * math.log2(p)
            
    return -entropy
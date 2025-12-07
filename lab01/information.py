import math

def calculate_information(probability):
    """
    Calculates the self-information of an event.
    Formula: I(x) = -log2(p(x))
    
    Args:
        probability (float): The probability of the event (0 < p <= 1).
    Returns:
        float: Information in bits.
    """
    if probability <= 0:
        return 0.0
    return -math.log2(probability)
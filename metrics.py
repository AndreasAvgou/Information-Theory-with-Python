def calculate_average_length(probabilities, codes):
    """
    Calculates the Average Codeword Length (L).
    Formula: L = sum(P(i) * length(code(i)))
    """
    avg_length = 0.0
    for symbol, prob in probabilities.items():
        code_len = len(codes[symbol])
        avg_length += prob * code_len
        
    return avg_length
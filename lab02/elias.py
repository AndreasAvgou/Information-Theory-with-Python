import math

def float_to_binary(num, length):
    """Converts float fraction to binary string."""
    binary = ""
    for _ in range(length):
        num *= 2
        if num >= 1:
            binary += "1"
            num -= 1
        else:
            binary += "0"
    return binary

def build_elias_codes(probs_map):
    """
    Shannon-Fano-Elias coding.
    Input: Dictionary {char: probability}
    """
    symbols = list(probs_map.keys())
    probs = list(probs_map.values())
    codes = {}
    cumulative = 0.0
    
    for i, char in enumerate(symbols):
        p = probs[i]
        # F_bar = Cumulative + p/2
        f_bar = cumulative + (p / 2.0)
        # Length = ceil(-log2(p)) + 1
        length = math.ceil(-math.log2(p)) + 1
        
        codes[char] = float_to_binary(f_bar, length)
        cumulative += p
        
    return codes
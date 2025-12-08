def build_fano_codes(sorted_items):
    """
    Recursive Shannon-Fano algorithm.
    Input: List of tuples [(char, freq)] sorted by frequency descending.
    """
    codes = {char: "" for char, freq in sorted_items}

    def recursive_split(subset):
        if len(subset) < 2:
            return

        total_weight = sum(item[1] for item in subset)
        current_weight = 0
        split_idx = 0
        min_diff = float('inf')

        # Find optimal split point
        for i in range(len(subset) - 1):
            current_weight += subset[i][1]
            diff = abs(2 * current_weight - total_weight)
            if diff < min_diff:
                min_diff = diff
                split_idx = i
            else:
                break
        
        # Split and assign bits
        left = subset[:split_idx + 1]
        right = subset[split_idx + 1:]

        for c, f in left:
            codes[c] += "0"
        for c, f in right:
            codes[c] += "1"

        recursive_split(left)
        recursive_split(right)

    recursive_split(sorted_items)
    return codes
def fano_encoding(sorted_probs):
    """
    Generates Fano codes for the given probabilities.
    Input: List of tuples [(letter, probability), ...] sorted by probability descending.
    Output: Dictionary {letter: binary_code_string}
    """
    # Base case: if only one symbol, no code needed (or dealt with in recursion)
    # However, if the initial call has 1 item, it's trivial.
    # We maintain a dictionary for codes.
    codes = {symbol: "" for symbol, prob in sorted_probs}
    
    def recursive_split(subset):
        """
        Helper function to recursively split the list and assign bits.
        """
        if len(subset) < 2:
            return

        # Find the best split point to balance probabilities
        # We want sum(left) approx sum(right)
        total = sum(p for s, p in subset)
        running_sum = 0.0
        split_index = 0
        min_diff = float('inf')

        for i in range(len(subset) - 1):
            running_sum += subset[i][1]
            # Calculate difference between left part and right part
            # Right part sum = Total - Left part sum
            # Diff = |Left - (Total - Left)| = |2*Left - Total|
            diff = abs(2 * running_sum - total)
            
            if diff < min_diff:
                min_diff = diff
                split_index = i
            else:
                # Since list is sorted, if diff starts increasing, we stop
                # (Though strictly, local minima check is safer, this works for Fano)
                break
        
        # Split the list
        # Index is inclusive for the left group
        left_group = subset[:split_index + 1]
        right_group = subset[split_index + 1:]

        # Assign '0' to the first group and '1' to the second group
        for symbol, prob in left_group:
            codes[symbol] += "0"
        
        for symbol, prob in right_group:
            codes[symbol] += "1"

        # Recurse
        recursive_split(left_group)
        recursive_split(right_group)

    # Start recursion
    recursive_split(sorted_probs)
    return codes
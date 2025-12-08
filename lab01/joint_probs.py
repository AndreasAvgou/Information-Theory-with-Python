def calculate_joint_probabilities(p_x, p_y):
    """
    Calculates joint probabilities for two independent binary events X and Y.
    Example: Rain (X) and Wind (Y).
    
    Returns:
        dict: Mapping of outcomes to their joint probabilities.
    """
    # Probabilities for "No" outcome (1 - p)
    p_not_x = 1.0 - p_x
    p_not_y = 1.0 - p_y

    # Independent events: P(A,B) = P(A) * P(B)
    joint_map = {
        "Yes, Yes": p_x * p_y,
        "Yes, No ": p_x * p_not_y,
        "No, Yes ": p_not_x * p_y,
        "No, No  ": p_not_x * p_not_y
    }
    
    return joint_map
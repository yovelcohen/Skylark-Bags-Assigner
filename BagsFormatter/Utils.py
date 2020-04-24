def get_max_carry_in_kg(max_percentage_allowed, warrior_weight):
    """
    This function receives the percentage of body weight warrior is allowed to carry and is body weight
    and returns the maximum weight he can carry.
    """
    max_weight_allowed = (max_percentage_allowed * warrior_weight) / 100.0
    return max_weight_allowed

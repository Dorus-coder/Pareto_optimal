def dominates(x, y):
    """
    Check if x dominates y (minimization problem).
    Returns True if x dominates y, False otherwise.
    """
    return all(x[i] <= y[i] for i in range(len(x))) and any(x[i] < y[i] for i in range(len(x)))
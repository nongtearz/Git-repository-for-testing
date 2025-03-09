import random

def guess_int(start, stop):
    """Generates a random integer between start and stop.

    Args:
        start (int): Lower bound.
        stop (int): Upper bound.

    Returns:
        int: A random integer.

    Raises:
        ValueError: If start > stop or inputs are not integers.
    """
    if not (isinstance(start, int) and isinstance(stop, int)):
        raise ValueError("start and stop must be integers")
    if start > stop:
        raise ValueError("start must be less than or equal to stop")
    return random.randint(start, stop)

def guess_float(start, stop):
    """Generates a random float between start and stop.

    Args:
        start (float): Lower bound.
        stop (float): Upper bound.

    Returns:
        float: A random float.

    Raises:
        ValueError: If start > stop.
    """
    if start > stop:
        raise ValueError("start must be less than or equal to stop")
    return random.uniform(start, stop)
def staircase(n, display):
    """Builds a staircase pattern using a specified character.

    Args:
        n (int): Size of the staircase.
        display (str): The character to use for the staircase.

    Returns:
        str: The staircase pattern.

    Raises:
        ValueError: If n is out of range or display is not a single character.
    """
    if not (0 < n <= 30):
        raise ValueError("n must be between 1 and 30")
    if not (isinstance(display, str) and len(display) == 1):
        raise ValueError("display must be a single character")
    result = []
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        chars = display * i
        result.append(spaces + chars)
    return "\n".join(result)
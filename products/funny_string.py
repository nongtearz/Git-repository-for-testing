import logging

logging.basicConfig(level=logging.INFO)

def funny_string(s):
    """Determines if a string is 'funny' based on ASCII differences.

    Args:
        s (str): The input string.

    Returns:
        str: "Funny" or "Not Funny".

    Raises:
        ValueError: If string length is out of range.
    """
    if not (1 <= len(s) <= 10000):
        raise ValueError("String length must be between 1 and 10000")
    
    r = s[::-1]
    
    for i in range(1, len(s)):
        diff_s = abs(ord(s[i]) - ord(s[i-1]))
        diff_r = abs(ord(r[i]) - ord(r[i-1]))
        if diff_s != diff_r:
            logging.info(f"String {s} is not funny at position {i}")
            return "Not Funny"
    
    return "Funny"
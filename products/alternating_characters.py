import logging

logging.basicConfig(level=logging.INFO)

def alternating_characters(s):
    """Counts the minimum number of deletions needed to make a string have no adjacent identical characters.

    Args:
        s (str): A string containing only 'A' and 'B'.

    Returns:
        int: The number of deletions required.

    Raises:
        ValueError: If the string length is invalid or contains invalid characters.
    """
    if not (1 <= len(s) <= 10**5):
        raise ValueError("String length must be between 1 and 10^5")
    if not all(c in 'AB' for c in s):
        raise ValueError("String must contain only A and B")
    
    deletions = 0
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            deletions += 1
            logging.info(f"Deletion required at index {i}: {s[i-1]} matches {s[i]}")
    
    return deletions
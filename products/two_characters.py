def two_characters(s):
    """Finds the length of the longest substring using exactly two distinct characters with no adjacent duplicates.

    Args:
        s (str): The input string.

    Returns:
        int: The length of the longest valid substring.
    """
    unique_chars = set(s)
    max_length = 0
    remaining_length = len(s)
    
    for char1 in unique_chars:
        for char2 in unique_chars:
            if char1 != char2:
                filtered = [c for c in s if c == char1 or c == char2]
                if len(filtered) <= max_length:
                    continue
                if all(filtered[i] != filtered[i+1] for i in range(len(filtered)-1)):
                    max_length = max(max_length, len(filtered))
    
    return max_length
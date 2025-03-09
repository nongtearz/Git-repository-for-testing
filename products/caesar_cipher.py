import logging

logging.basicConfig(level=logging.INFO)

def caesar_cipher(s, k):
    """Encrypts a string using the Caesar cipher with a given shift.

    Args:
        s (str): The input string containing alphabets and hyphens.
        k (int): The number of positions to shift each letter.

    Returns:
        str: The encrypted string.

    Raises:
        ValueError: If the string is empty or contains invalid characters.
    """
    if not s:
        raise ValueError("String cannot be empty")
    
    k = k % 26
    
    result = ""
    for char in s:
        if char.isalpha():
            ascii_base = 65 if char.isupper() else 97
            shifted = (ord(char) - ascii_base + k) % 26
            result += chr(shifted + ascii_base)
        elif char == '-':
            result += char
        else:
            logging.warning(f"Invalid character '{char}' encountered in string.")
            raise ValueError("String must contain only alphabets and hyphens")
            
    return result
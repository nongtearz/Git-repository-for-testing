def is_prime_list(numbers):
    """Checks if all numbers in a list are prime.

    Args:
        numbers (list): A list of integers.

    Returns:
        bool: True if all numbers are prime or the list is empty, False otherwise.
    """
    if not numbers:
        return True  # Changed behavior for empty list
    
    for num in numbers:
        if num <= 1:
            return False
        for n in range(2, int(num ** 0.5) + 1):
            if num % n == 0:
                return False
    return True
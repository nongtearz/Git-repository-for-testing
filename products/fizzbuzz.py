def fizzbuzz(x):
    """Returns FizzBuzz string based on divisibility by 3 and 5.

    Args:
        x (int): The input number.

    Returns:
        str: "FizzBuzz", "Fizz", "Buzz", or "not FizzBuzz".
    """
    if x % 3 == 0 and x % 5 == 0:
        return "FizzBuzz"
    elif x % 3 == 0:
        return "Fizz"
    elif x % 5 == 0:
        return "Buzz"
    else:
        return "not FizzBuzz"
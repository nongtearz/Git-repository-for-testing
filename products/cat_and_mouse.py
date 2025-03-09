import logging

logging.basicConfig(level=logging.INFO)

def cat_and_mouse(x, y, z):
    """Determines which cat catches the mouse first or if the mouse escapes.

    Args:
        x (int): Position of Cat A.
        y (int): Position of Cat B.
        z (int): Position of Mouse C.

    Returns:
        str: "Cat A", "Cat B", or "Mouse C".

    Raises:
        ValueError: If positions are out of range.
    """
    if not (1 <= x <= 100 and 1 <= y <= 100 and 1 <= z <= 100):
        raise ValueError("Positions must be between 1 and 100")
    
    dist_a = abs(x - z)
    dist_b = abs(y - z)
    
    if dist_a < dist_b:
        return "Cat A"
    elif dist_b < dist_a:
        return "Cat B"
    else:
        logging.info(f"Tie detected: Cat A and Cat B both at distance {dist_a}")
        return "Mouse C"
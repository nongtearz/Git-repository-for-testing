import logging

logging.basicConfig(level=logging.INFO)

def grid_challenge(grid):
    """Checks if a grid can be sorted row-wise to have columns in non-decreasing order.

    Args:
        grid (list): A list of strings representing the grid.

    Returns:
        str: "YES" or "NO".

    Raises:
        ValueError: If grid is empty or rows have inconsistent lengths.
    """
    if not grid:
        raise ValueError("Grid cannot be empty")
    if not all(len(row) == len(grid[0]) for row in grid):
        raise ValueError("All rows must have the same length")
    
    sorted_rows = [sorted(row) for row in grid]
    for col in range(len(sorted_rows[0])):
        for row in range(len(sorted_rows) - 1):
            if sorted_rows[row][col] > sorted_rows[row + 1][col]:
                logging.info(f"Column {col} fails at rows {row} and {row+1}")
                return "NO"
    return "YES"
from products.grid_challenge import grid_challenge
import unittest

# Last modified: 2025-03-09
class TestGridChallenge(unittest.TestCase):
    def test_grid_challenge_sorted_grid(self):
        grid = ["abc", "ade", "efg"]
        expected = "YES"
        self.assertEqual(grid_challenge(grid), expected)

    def test_grid_challenge_unsorted_grid(self):
        grid = ["ebc", "ade", "efg"]
        expected = "NO"
        self.assertEqual(grid_challenge(grid), expected)

    def test_grid_challenge_single_row(self):
        grid = ["zxy"]
        expected = "YES"
        self.assertEqual(grid_challenge(grid), expected)

    def test_grid_challenge_identical_rows(self):
        grid = ["aaa", "aaa", "aaa"]
        expected = "YES"
        self.assertEqual(grid_challenge(grid), expected)

    def test_grid_challenge_empty_grid(self):
        grid = []
        with self.assertRaises(ValueError) as context:
            grid_challenge(grid)
        self.assertEqual(str(context.exception), "Grid cannot be empty")

    def test_grid_challenge_inconsistent_rows(self):
        grid = ["abc", "ab", "abcd"]
        with self.assertRaises(ValueError) as context:
            grid_challenge(grid)
        self.assertEqual(str(context.exception), "All rows must have the same length")

    def test_grid_challenge_single_column(self):
        grid = ["a", "b", "c"]
        expected = "YES"
        self.assertEqual(grid_challenge(grid), expected)
from products.staircase import staircase
import unittest

# Last modified: 2025-03-09
class TestStaircase(unittest.TestCase):
    def test_staircase_size_4_with_hash(self):
        n = 4
        display = "#"
        expected = "   #\n  ##\n ###\n####"
        result = staircase(n, display)
        self.assertEqual(result, expected)

    def test_staircase_size_1_with_star(self):
        n = 1
        display = "*"
        expected = "*"
        result = staircase(n, display)
        self.assertEqual(result, expected)

    def test_staircase_size_3_with_dollar(self):
        n = 3
        display = "$"
        expected = "  $\n $$\n$$$"
        result = staircase(n, display)
        self.assertEqual(result, expected)

    def test_staircase_max_size(self):
        n = 30
        display = "#"
        result = staircase(n, display)
        self.assertEqual(len(result.split("\n")), 30)
        self.assertEqual(result.split("\n")[-1], "#" * 30)

    def test_staircase_invalid_n_zero(self):
        n = 0
        display = "#"
        with self.assertRaises(ValueError) as context:
            staircase(n, display)
        self.assertEqual(str(context.exception), "n must be between 1 and 30")

    def test_staircase_invalid_n_negative(self):
        n = -1
        display = "#"
        with self.assertRaises(ValueError) as context:
            staircase(n, display)
        self.assertEqual(str(context.exception), "n must be between 1 and 30")

    def test_staircase_invalid_n_above_range(self):
        n = 31
        display = "#"
        with self.assertRaises(ValueError) as context:
            staircase(n, display)
        self.assertEqual(str(context.exception), "n must be between 1 and 30")

    def test_staircase_invalid_display(self):
        n = 3
        display = "ab"
        with self.assertRaises(ValueError) as context:
            staircase(n, display)
        self.assertEqual(str(context.exception), "display must be a single character")
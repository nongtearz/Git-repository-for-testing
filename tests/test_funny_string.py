from products.funny_string import funny_string
import unittest

# Last modified: 2025-03-09
class TestFunnyString(unittest.TestCase):
    def test_funny_string(self):
        s = "acxz"
        expected = "Funny"
        result = funny_string(s)
        self.assertEqual(result, expected)

    def test_not_funny_string(self):
        s = "bcxz"
        expected = "Not Funny"
        result = funny_string(s)
        self.assertEqual(result, expected)

    def test_single_char(self):
        s = "a"
        expected = "Funny"
        result = funny_string(s)
        self.assertEqual(result, expected)

    def test_length_out_of_range_low(self):
        s = ""
        with self.assertRaises(ValueError) as context:
            funny_string(s)
        self.assertEqual(str(context.exception), "String length must be between 1 and 10000")

    def test_length_out_of_range_high(self):
        s = "a" * 10001
        with self.assertRaises(ValueError) as context:
            funny_string(s)
        self.assertEqual(str(context.exception), "String length must be between 1 and 10000")

    def test_long_funny_string(self):
        s = "ab" + "c" * 9996 + "yz"  # Length 10000, funny
        expected = "Funny"
        result = funny_string(s)
        self.assertEqual(result, expected)
from products.alternating_characters import alternating_characters
import unittest

# Last modified: 2025-03-09
class TestAlternatingCharacters(unittest.TestCase):
    def test_all_same_chars(self):
        s = "AAAA"
        expected = 3
        result = alternating_characters(s)
        self.assertEqual(result, expected)

    def test_already_alternating(self):
        s = "ABABABAB"
        expected = 0
        result = alternating_characters(s)
        self.assertEqual(result, expected)

    def test_mixed_repetitions(self):
        s = "AABABBAA"
        expected = 3
        result = alternating_characters(s)
        self.assertEqual(result, expected)

    def test_single_character(self):
        s = "A"
        expected = 0
        result = alternating_characters(s)
        self.assertEqual(result, expected)

    def test_length_out_of_range_low(self):
        s = ""
        with self.assertRaises(ValueError) as context:
            alternating_characters(s)
        self.assertEqual(str(context.exception), "String length must be between 1 and 10^5")

    def test_length_out_of_range_high(self):
        s = "A" * (10**5 + 1)
        with self.assertRaises(ValueError) as context:
            alternating_characters(s)
        self.assertEqual(str(context.exception), "String length must be between 1 and 10^5")

    def test_invalid_characters(self):
        s = "AACB"
        with self.assertRaises(ValueError) as context:
            alternating_characters(s)
        self.assertEqual(str(context.exception), "String must contain only A and B")

    def test_long_string(self):
        s = "A" * 50000 + "B" * 50000
        expected = 99998  # One deletion at the boundary
        result = alternating_characters(s)
        self.assertEqual(result, expected)
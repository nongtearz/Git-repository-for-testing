from products.two_characters import two_characters
import unittest

# Last modified: 2025-03-09
class TestTwoCharacters(unittest.TestCase):
    def test_mixed_characters(self):
        s = "beabeefeab"
        expected = 5
        self.assertEqual(two_characters(s), expected)

    def test_all_same_characters(self):
        s = "aaaa"
        expected = 0
        self.assertEqual(two_characters(s), expected)

    def test_alternating_characters(self):
        s = "abababab"
        expected = 8
        self.assertEqual(two_characters(s), expected)

    def test_single_character(self):
        s = "a"
        expected = 0
        self.assertEqual(two_characters(s), expected)

    def test_empty_string(self):
        s = ""
        expected = 0
        self.assertEqual(two_characters(s), expected)

    def test_three_repeating_characters(self):
        s = "abcabcabc"
        expected = 6
        self.assertEqual(two_characters(s), expected)

    def test_long_mixed_string(self):
        s = "ab" * 50000
        expected = 100000
        self.assertEqual(two_characters(s), expected)
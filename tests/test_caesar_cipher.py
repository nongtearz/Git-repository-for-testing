from products.caesar_cipher import caesar_cipher
import unittest

# Last modified: 2025-03-09
class TestCaesarCipher(unittest.TestCase):
    def test_basic_rotation(self):
        s = "abc"
        k = 1
        expected = "bcd"
        result = caesar_cipher(s, k)
        self.assertEqual(result, expected)

    def test_case_preservation(self):
        s = "AbC"
        k = 2
        expected = "CdE"
        result = caesar_cipher(s, k)
        self.assertEqual(result, expected)

    def test_large_rotation(self):
        s = "xyz"
        k = 27
        expected = "yza"
        result = caesar_cipher(s, k)
        self.assertEqual(result, expected)

    def test_zero_rotation(self):
        s = "abc"
        k = 0
        expected = "abc"
        result = caesar_cipher(s, k)
        self.assertEqual(result, expected)

    def test_with_hyphen(self):
        s = "middle-outz"
        k = 2
        expected = "okffng-qwvb"
        result = caesar_cipher(s, k)
        self.assertEqual(result, expected)

    def test_single_character(self):
        s = "a"
        k = 1
        expected = "b"
        result = caesar_cipher(s, k)
        self.assertEqual(result, expected)

    def test_empty_string(self):
        s = ""
        k = 3
        with self.assertRaises(ValueError) as context:
            caesar_cipher(s, k)
        self.assertEqual(str(context.exception), "String cannot be empty")

    def test_invalid_characters(self):
        s = "hello@world"
        k = 3
        with self.assertRaises(ValueError) as context:
            caesar_cipher(s, k)
        self.assertEqual(str(context.exception), "String must contain only alphabets and hyphens")

    def test_mixed_case_with_multiple_hyphens(self):
        s = "Hello-World-Test"
        k = 1
        expected = "Ifmmp-Xpsme-Uftu"
        result = caesar_cipher(s, k)
        self.assertEqual(result, expected)
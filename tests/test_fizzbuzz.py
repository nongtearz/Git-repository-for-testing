from products.fizzbuzz import fizzbuzz
import unittest

# Last modified: 2025-03-09
class TestFizzBuzz(unittest.TestCase):
    def test_divisible_by_3_and_5(self):
        self.assertEqual(fizzbuzz(15), "FizzBuzz")
        self.assertEqual(fizzbuzz(30), "FizzBuzz")

    def test_divisible_by_3_only(self):
        self.assertEqual(fizzbuzz(3), "Fizz")
        self.assertEqual(fizzbuzz(9), "Fizz")

    def test_divisible_by_5_only(self):
        self.assertEqual(fizzbuzz(5), "Buzz")
        self.assertEqual(fizzbuzz(10), "Buzz")

    def test_not_divisible_by_3_or_5(self):
        self.assertEqual(fizzbuzz(7), "not FizzBuzz")
        self.assertEqual(fizzbuzz(11), "not FizzBuzz")

    def test_zero(self):
        self.assertEqual(fizzbuzz(0), "FizzBuzz")

    def test_negative_number(self):
        self.assertEqual(fizzbuzz(-15), "FizzBuzz")
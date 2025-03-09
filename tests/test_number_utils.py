from products.number_utils import is_prime_list
import unittest

# Last modified: 2025-03-09
class PrimeListTest(unittest.TestCase):
    def test_empty_list(self):
        prime_list = []
        result = is_prime_list(prime_list)
        self.assertTrue(result)  # Updated behavior

    def test_all_primes(self):
        prime_list = [2, 3, 5, 7]
        result = is_prime_list(prime_list)
        self.assertTrue(result)

    def test_contains_non_prime(self):
        prime_list = [2, 3, 4, 7]
        result = is_prime_list(prime_list)
        self.assertFalse(result)

    def test_contains_less_than_one(self):
        prime_list = [2, 0, 5]
        result = is_prime_list(prime_list)
        self.assertFalse(result)

    def test_contains_one(self):
        prime_list = [1]
        result = is_prime_list(prime_list)
        self.assertFalse(result)

    def test_negative_number(self):
        prime_list = [-2, 3, 5]
        result = is_prime_list(prime_list)
        self.assertFalse(result)

    def test_single_prime(self):
        prime_list = [11]
        result = is_prime_list(prime_list)
        self.assertTrue(result)

    def test_single_non_prime(self):
        prime_list = [4]
        result = is_prime_list(prime_list)
        self.assertFalse(result)

    def test_large_prime_numbers(self):
        prime_list = [997, 991]
        result = is_prime_list(prime_list)
        self.assertTrue(result)
from products.guess import guess_int, guess_float
import unittest
from unittest.mock import patch

# Last modified: 2025-03-09
class TestRandomGuess(unittest.TestCase):
    @patch('random.randint')
    def test_guess_int_within_range(self, mock_randint):
        mock_randint.return_value = 5
        start, stop = 1, 10
        result = guess_int(start, stop)
        self.assertEqual(result, 5)
        self.assertIsInstance(result, int)
        mock_randint.assert_called_with(start, stop)

    @patch('random.uniform')
    def test_guess_float_within_range(self, mock_uniform):
        mock_uniform.return_value = 5.5
        start, stop = 1.0, 10.0
        result = guess_float(start, stop)
        self.assertEqual(result, 5.5)
        self.assertIsInstance(result, float)
        mock_uniform.assert_called_with(start, stop)

    @patch('random.randint')
    def test_guess_int_same_start_stop(self, mock_randint):
        mock_randint.return_value = 5
        start, stop = 5, 5
        result = guess_int(start, stop)
        self.assertEqual(result, 5)
        mock_randint.assert_called_with(start, stop)

    @patch('random.uniform')
    def test_guess_float_same_start_stop(self, mock_uniform):
        mock_uniform.return_value = 7.5
        start, stop = 7.5, 7.5
        result = guess_float(start, stop)
        self.assertEqual(result, 7.5)
        mock_uniform.assert_called_with(start, stop)

    @patch('random.randint')
    def test_guess_int_negative_range(self, mock_randint):
        mock_randint.return_value = -5
        start, stop = -10, -1
        result = guess_int(start, stop)
        self.assertEqual(result, -5)
        self.assertIsInstance(result, int)
        mock_randint.assert_called_with(start, stop)

    def test_guess_int_invalid_range(self):
        start, stop = 10, 1
        with self.assertRaises(ValueError) as context:
            guess_int(start, stop)
        self.assertEqual(str(context.exception), "start must be less than or equal to stop")

    def test_guess_float_invalid_range(self):
        start, stop = 10.0, 1.0
        with self.assertRaises(ValueError) as context:
            guess_float(start, stop)
        self.assertEqual(str(context.exception), "start must be less than or equal to stop")

    def test_guess_int_invalid_type(self):
        start, stop = "1", 10
        with self.assertRaises(ValueError) as context:
            guess_int(start, stop)
        self.assertEqual(str(context.exception), "start and stop must be integers")
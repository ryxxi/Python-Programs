from unittest import TestCase
from primefunction import find_prime

class TestPrimeFunction(TestCase):

	def test_function_exists(self):

		find_prime(7)

	def test_function_returns_true(self):

		actual = find_prime(12)
		expected = "Is not prime"
		self.assertEqual(actual, expected)

		actual = find_prime(13)
		expected = "Is prime"
		self.assertEqual(actual, expected)

	def test_function_raises_exception_for_invalid_inputs(self):

		self.assertRaises(TypeError, find_prime, 12.5)
		self.assertRaises(TypeError, find_prime, True)
		self.assertRaises(TypeError, find_prime, "yes")
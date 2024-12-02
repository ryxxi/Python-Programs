from unittest import TestCase
from primesbeforefunction import get_primes_before

class TestPrimesBeforeFunction(TestCase):

	def test_function_exists(self):

		get_primes_before(9)

	def test_function_returns_correctly(self):

		actual = get_primes_before(9)
		expected = [2, 3, 5, 7]
		self.assertEqual(actual, expected)

	def test_function_raises_exception_with_invalid_inputs(self):

		self.assertRaises(TypeError, get_primes_before, None)
		self.assertRaises(TypeError, get_primes_before, True)
		self.assertRaises(ValueError, get_primes_before, -21)
		self.assertRaises(TypeError, get_primes_before, "hello")


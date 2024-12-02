from unittest import TestCase
from evensumfunction import get_even_sum

class TestEvenSumFunction(TestCase):

	def test_function_exists(self):

		get_even_sum([1,2,3,4,5])

	def test_function_returns_correctly(self):

		actual = get_even_sum([1,2,3,4,5])
		expected = 6
		self.assertEqual(actual, expected)

	def test_function_raises_exception_with_invalid_inputs(self):

		self.assertRaises(TypeError, get_even_sum, None)
		self.assertRaises(TypeError, get_even_sum, True)


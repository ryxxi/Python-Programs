from unittest import TestCase
from listaveragefunction import get_average

class TestAverageFunction(TestCase):

	def test_function_exists(self):

		integers = [1, 3, 8, 6, 4]
		get_average(integers)

	def test_fuctions_returns_true(self):

		integers = [1, 2, 3, 4, 5, 6, 7, 8]
		actual = get_average(integers)
		expected = 4.5
		self.assertEqual(actual, expected)

		integers = [1.5, 2.5, 3]
		actual = get_average(integers)
		expected = 7/3
		self.assertEqual(actual, expected)

	def test_function_raises_exception_for_invalid_inputs(self):

		mixed_list = [1.5, 2.5, 3, "hello", True]
		self.assertRaises(TypeError, get_average, mixed_list)
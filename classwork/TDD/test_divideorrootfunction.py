from unittest import TestCase
from divideorrootfunction import get_root_or_remainder

class TestDivideOrRootFunction(TestCase):

	def test_function_exists(self):
		get_root_or_remainder(5)

	def test_function_returns_correct_remainder_for_int(self):
		actual = get_root_or_remainder(9)
		expected = 4
		self.assertEqual(actual, expected)

	def test_function_returns_correct_root_for_int(self):
		actual = get_root_or_remainder(20)
		expected = 20 ** 0.5
		self.assertEqual(actual, expected)

	def test_function_returns_correct_remainder_for_float(self):
		actual = get_root_or_remainder(23.9)
		expected = 23.9 % 5
		self.assertEqual(actual, expected)

	def test_function_returns_correct_remainder_for_neg_int(self):
		actual = get_root_or_remainder(-29)
		expected = 4

	def test_function_raises_error_with_negative_multiple_of_five(self):
		self.assertRaises(ValueError, get_root_or_remainder, -5)

	def test_function_raises_error_with_invalid_types(self):
		self.assertRaises(TypeError, get_root_or_remainder, "hello")
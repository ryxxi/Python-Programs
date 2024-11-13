from unittest import TestCase
from onlyfloatsfunction import get_floats

class TestOnlyFloatsFunction(TestCase):

	def test_function_exists(self):
		get_floats(2.3, 8)

	def test_returns_correct_values_for_two_floats(self):
		actual = get_floats(6.9, 4.9)
		expected = 2
		self.assertEqual(actual, expected)

		actual = get_floats(2.9, 9.0)
		expected = 2
		self.assertEqual(actual, expected)

		actual = get_floats(8.12, 4.378)
		expected = 2
		self.assertEqual(actual, expected)

	def test_returns_correct_values_for_one_float(self):

		actual = get_floats(6.9, 4)
		expected = 1
		self.assertEqual(actual, expected)

		actual = get_floats(6, 4.9)
		expected = 1
		self.assertEqual(actual, expected)

	def test_returns_correct_values_for_no_floats(self):
		
		actual = get_floats(6, 4)
		expected = 0
		self.assertEqual(actual, expected)

		actual = get_floats("hi", True)
		expected = 0
		self.assertEqual(actual, expected)

		actual = get_floats(200, False)
		expected = 0
		self.assertEqual(actual, expected)
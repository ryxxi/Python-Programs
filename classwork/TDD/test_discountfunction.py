from unittest import TestCase
from discountfunction import get_discount

class TestDiscountFunction(TestCase):

	def test_function_exists(self):
		get_discount(50, 12)

	def test_function_returns_correct_values_for_ints(self):
		actual = get_discount(150, 15)
		expected = 127.50
		self.assertEqual(actual, expected)

	def test_function_returns_correct_values_for_floats(self):
		actual = get_discount(150.75, 20.5)
		expected = 119.85
		self.assertEqual(actual, expected)

	def test_function_raises_error_for_negative_original_price(self):
		argument_list = [-150, 15]
		self.assertRaises(ValueError, get_discount, argument_list[0], argument_list[1])

	def test_function_raises_error_for_negative_discount(self):
		argument_list = [150, -15]
		self.assertRaises(ValueError, get_discount, argument_list[0], argument_list[1])

	def test_function_raises_error_for_negative_inputs(self):
		argument_list = [-150, -15]
		self.assertRaises(ValueError, get_discount, argument_list[0], argument_list[1])

	def test_function_raises_error_for_invalid_inputs(self):
		argument_list = ["hello", 20]
		self.assertRaises(TypeError, get_discount, argument_list[0], argument_list[1])

		argument_list = [300, "**"]
		self.assertRaises(TypeError, get_discount, argument_list[0], argument_list[1])

		argument_list = [True, "number1"]
		self.assertRaises(TypeError, get_discount, argument_list[0], argument_list[1])






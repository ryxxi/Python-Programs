from unittest import TestCase
from discountfunction import get_discount
from onlyfloatsfunction import get_floats
from futureinvestmentfunction import get_future_investment_value
from divideorrootfunction import get_root_or_remainder

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

	def test_function_raises_error_with_no_arguments(self):
		self.assertRaises(TypeError, get_discount)

	def test_function_raises_error_with_missing_arguments(self):
		argument_list = [100]
		self.assertRaises(TypeError, get_discount, argument_list[0])




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

	def test_function_raises_error_with_no_arguments(self):
		self.assertRaises(TypeError, get_floats)

	def test_function_raises_error_with_missing_arguments(self):
		argument_list = [12]
		self.assertRaises(TypeError, get_floats, argument_list[0])


class TestFutureInvestmentFunction(TestCase):

	def test_function_exists(self):
		get_future_investment_value(10000, 4.6, 4)

	def test_function_returns_correct_value_with_positive_monthly_interest(self):
		actual = get_future_investment_value(10000, 4.6, 4)
		expected = 86600.59

	def test_function_returns_correct_value_with_negative_monthly_interest(self):
		actual = get_future_investment_value(10000, -4.6, 4)
		expected = 1043.09

	def test_function_raises_error_with_negative_principal(self):
		argument_list = [-5000, 2.9, 6]
		self.assertRaises(ValueError, get_future_investment_value, argument_list[0], argument_list[1], argument_list[2])

	def test_function_raises_error_with_negative_years(self):
		argument_list = [5000, 2.9, -6]
		self.assertRaises(ValueError, get_future_investment_value, argument_list[0], argument_list[1], argument_list[2])

	def test_function_raises_error_with_negative_principal_and_years(self):
		argument_list = [-5000, 2.9, -6]
		self.assertRaises(ValueError, get_future_investment_value, argument_list[0], argument_list[1], argument_list[2])

	def test_function_raises_error_with_invalid_types(self):
		argument_list = [5000, 2.9, "hello"]
		self.assertRaises(TypeError, get_future_investment_value, argument_list[0], argument_list[1], argument_list[2])

		argument_list = ["hi", 2.9, 6]
		self.assertRaises(TypeError, get_future_investment_value, argument_list[0], argument_list[1], argument_list[2])

		argument_list = [5000, "howdy", 6]
		self.assertRaises(TypeError, get_future_investment_value, argument_list[0], argument_list[1], argument_list[2])

	def test_function_raises_error_with_no_arguments(self):
		self.assertRaises(TypeError, get_future_investment_value)

	def test_function_raises_error_with_missing_arguments(self):
		argument_list = [12, 7]
		self.assertRaises(TypeError, get_future_investment_value, argument_list[0], argument_list[1])

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
		self.assertRaises(TypeError, get_root_or_remainder, "**")

	def test_function_raises_error_with_missing_arguments(self):
		self.assertRaises(TypeError, get_root_or_remainder)


























from unittest import TestCase
from futureinvestmentfunction import get_future_investment_value

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




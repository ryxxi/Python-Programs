from unittest import TestCase
from productfunction import get_product

class ProductFunction(TestCase):

	def test_product_function_exists(self):
		get_product(3, 5)




	def test_product_function_returns_correctly_with_positive_ints(self):
		actual = get_product(5, 5)
		expected = 25
		self.assertEqual(actual, expected)

	def test_product_function_returns_correctly_with_a_negative_int(self):
		actual = get_product(5, -5)
		expected = -25
		self.assertEqual(actual, expected)

	def test_product_function_returns_correctly_with_negative_ints(self):
		actual = get_product(-5, -5)
		expected = 25
		self.assertEqual(actual, expected)




	def test_product_function_returns_correctly_with_positive_float_and_positive_int(self):
		actual = get_product(5.3, 5)
		expected = 26.5
		self.assertEqual(actual, expected)

	def test_product_function_returns_correctly_with_positive_float_and_negaive_int(self):
		actual = get_product(5.3, -5)
		expected = -26.5
		self.assertEqual(actual, expected)

	def test_product_function_returns_correctly_with_negative_float_and_positive_int(self):
		actual = get_product(-5.3, 5)
		expected = -26.5
		self.assertEqual(actual, expected)

	def test_product_function_returns_correctly_with_negative_float_and_negative_int(self):
		actual = get_product(-5.3, -5)
		expected = 26.5
		self.assertEqual(actual, expected)




	def test_product_function_returns_correctly_with_positive_floats(self):
		actual = get_product(2.4, 3.8)
		expected = 9.12
		self.assertEqual(actual, expected)

	def test_product_function_returns_correctly_with_a_negative_float(self):
		actual = get_product(-2.4, 3.8)
		expected = -9.12
		self.assertEqual(actual, expected)

	def test_product_function_returns_correctly_with_negative_floats(self):
		actual = get_product(-2.4, -3.8)
		expected = 9.12
		self.assertEqual(actual, expected)


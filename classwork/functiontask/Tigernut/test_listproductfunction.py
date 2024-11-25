from unittest import TestCase
from listproductfunction import get_product

class TestListProductFunction(TestCase):

	def test_function_exists(self):

		numberlist = [1, 2, 3, 4]
		get_product(numberlist)

	def test_function_returns_correctly(self):

		numberlist = [1, 2, 3, 4]
		actual = get_product(numberlist)
		expected = 24
		self.assertEqual(actual, expected)

	def test_function_raises_exceptions_for_invalid_inputs(self):

		self.assertRaises(TypeError, get_product, None)
		self.assertRaises(TypeError, get_product, "Hello")
		self.assertRaises(TypeError, get_product, [12, 34, "how"])
from unittest import TestCase
from productfunction import get_product

class TestProductFunction(TestCase):

	def test_if_function_exists(self):
		get_product(1, 2)

	def test_if_function_returns_correctly(self):
		actual = get_product(3, 5)
		expected = 15
		self.assertEqual(actual, expected)
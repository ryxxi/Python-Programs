from unittest import TestCase
from evensumfunction import get_even_sum

class TestEvenSumFunction(TestCase):

	def test_function_exists(self):

		integers = [1, 3, 8, 6, 4]
		get_even_sum(integers)

	def test_fuctions_returns_true(self):

		integers = [1, 2, 3, 4, 5, 6, 7, 8]
		actual = get_even_sum(integers)
		expected = 20
		self.assertEqual(actual, expected)

		integers = [1.5, 2.2, 3, 4, 59, 60, 76, 8.45]
		actual = get_even_sum(integers)
		expected = 140
		self.assertEqual(actual, expected)

		list_of_stuff = ["hello", 2, 12, "2"]
		actual = get_even_sum(list_of_stuff)
		expected = 14
		self.assertEqual(actual, expected)
from unittest import TestCase
from palindromefunction import get_palindrome

class TestEvenSumFunction(TestCase):

	def test_function_exists(self):

		get_palindrome("hello")

	def test_fuctions_returns_true(self):

		actual = get_palindrome("nice")
		expected = False
		self.assertEqual(actual, expected)

		actual = get_palindrome("yessey")
		expected = True
		self.assertEqual(actual, expected)

	def test_function_raises_exception_for_invalid_inputs(self):

		self.assertRaises(TypeError, get_palindrome, 12)
		self.assertRaises(TypeError, get_palindrome, 12.65)
		self.assertRaises(TypeError, get_palindrome, False)
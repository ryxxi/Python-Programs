from unittest import TestCase
from anagramfunction import find_anagram

class TestAnagramFunction(TestCase):

	def test_function_exists(self):

		find_anagram("hello", "twelve")

	def test_fuction_returns_true(self):

		actual = find_anagram("hello", "nicely")
		expected = False
		self.assertEqual(actual, expected)

		actual = find_anagram("spear", "reaps")
		expected = True
		self.assertEqual(actual, expected)

	def test_raises_exception_for_invalid_inputs(self):

		self.assertRaises(TypeError, find_anagram, 12, "hello")
		self.assertRaises(TypeError, find_anagram, True, "yes")
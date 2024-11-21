from unittest import TestCase
from vowelfinder import get_vowels

class TestGetVowel(TestCase):

	def test_function_exists(self):

		get_vowels("hello")

	def test_fuction_returns_true(self):

		actual = get_vowels("hello")
		expected = 2
		self.assertEqual(actual, expected)

	def test_raises_exception_for_invalid_inputs(self):

		self.assertRaises(TypeError, get_vowels, 12)
		self.assertRaises(TypeError, get_vowels, True)
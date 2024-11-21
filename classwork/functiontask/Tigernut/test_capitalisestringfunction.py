from unittest import TestCase
from capitalisestringfunction import capitalise

class TestAverageFunction(TestCase):

	def test_function_exists(self):

		strings = ["hello", "nice"]
		capitalise(strings)

	def test_fuctions_returns_true(self):

		strings = ["hello", "nice"]
		actual = capitalise(strings)
		expected = ["Hello", "Nice"]
		self.assertEqual(actual, expected)

		strings = ["Hi", "yellOw", "hOWDY"]
		actual = capitalise(strings)
		expected = ["Hi", "YellOw", "HOWDY"]
		self.assertEqual(actual, expected)

	def test_function_raises_exception_for_invalid_inputs(self):

		mixed_list = [1.5, "nice", 3, "hello", True]
		self.assertRaises(TypeError, capitalise, 12)
		self.assertRaises(TypeError, capitalise, mixed_list)
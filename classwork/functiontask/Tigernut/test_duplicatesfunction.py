from unittest import TestCase
from duplicatesfunction import check_duplicates

class TestAverageFunction(TestCase):

	def test_function_exists(self):

		string1 = ["hello", "nice"]
		string2 = ["hello"]
		check_duplicates(string1, string2)

	def test_fuctions_returns_true(self):

		string1 = ["hello", "nice"]
		string2 = ["hello"]
		actual = check_duplicates(string1, string2)
		expected = True
		self.assertEqual(actual, expected)

		string1 = ["hello", "nice"]
		string2 = ["howdy"]
		actual = check_duplicates(string1, string2)
		expected = False
		self.assertEqual(actual, expected)

	def test_function_raises_exception_for_invalid_inputs(self):

		self.assertRaises(TypeError, check_duplicates, 1, True)
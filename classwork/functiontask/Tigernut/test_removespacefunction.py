from unittest import TestCase
from removespacefunction import remove_space

class TestReverseStringFunction(TestCase):

	def test_function_exists(self):

		remove_space("hello world")

	def test_fuction_returns_true(self):

		actual = remove_space("hello i am leke")
		expected = "helloiamleke"
		self.assertEqual(actual, expected)

	def test_raises_exception_for_invalid_inputs(self):

		self.assertRaises(TypeError, remove_space, 12,)
		self.assertRaises(TypeError, remove_space, True)
from unittest import TestCase
from reversestringfunction import get_reverse

class TestReverseStringFunction(TestCase):

	def test_function_exists(self):

		get_reverse("hello")

	def test_fuction_returns_true(self):

		actual = get_reverse("hello")
		expected = "olleh"
		self.assertEqual(actual, expected)

		actual = get_reverse("hia")
		expected = "aih"
		self.assertEqual(actual, expected)

	def test_raises_exception_for_invalid_inputs(self):

		self.assertRaises(TypeError, get_reverse, 12,)
		self.assertRaises(TypeError, get_reverse, True)
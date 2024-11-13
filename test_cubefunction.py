from unittest import TestCase
from cubefunction import get_cube

class TestCubeFunction(TestCase):

	def test_cube_function_exists(self):
		get_cube(3)

	def test_cube_function_returns_correctly(self):
		actual = get_cube(3)
		expected = 27
		self.assertEqual(actual, expected)
		actual = get_cube(0.1)
		expected = 0.001
		self.assertEqual(actual, expected)

	def test_cube_function_raises_exception_with_invalids(self):
		self.assertRaises(TypeError, get_cube, "string")
from unittest import TestCase
from allkatafunctions import is_even
from allkatafunctions import is_prime
from allkatafunctions import subtract
from allkatafunctions import divide
from allkatafunctions import factor_of
from allkatafunctions import is_square
from allkatafunctions import is_palindrome
from allkatafunctions import factorial_of
from allkatafunctions import square_of

class TestEvenFunction(TestCase):

	def test_function_exists(self):

		is_even(8)

	def test_function_returns_correctly(self):

		actual = is_even(7)
		expected = False
		self.assertEqual(actual, expected)

		actual = is_even(8)
		expected = True
		self.assertEqual(actual, expected)

	def test_function_raises_exceptions_for_invalid_inputs(self):

		self.assertRaises(TypeError, is_even, True)
		self.assertRaises(TypeError, is_even, "hello")




class TestPrimeFunction(TestCase):

	def test_function_exists(self):

		is_prime(8)

	def test_function_returns_correctly(self):

		actual = is_prime(8)
		expected = False
		self.assertEqual(actual, expected)

		actual = is_prime(7)
		expected = True
		self.assertEqual(actual, expected)

	def test_function_raises_exceptions_for_invalid_inputs(self):

		self.assertRaises(TypeError, is_prime, True)
		self.assertRaises(TypeError, is_prime, "hello")




class TestSubtractFunction(TestCase):

	def test_function_exists(self):

		subtract(8, 6)

	def test_function_returns_correctly(self):

		actual = subtract(8, 6)
		expected = 2
		self.assertEqual(actual, expected)

		actual = subtract(7, 10)
		expected = 3
		self.assertEqual(actual, expected)

	def test_function_raises_exceptions_for_invalid_inputs(self):

		self.assertRaises(TypeError, subtract, True)
		self.assertRaises(TypeError, subtract, "hello")




class TestDivideFunction(TestCase):

	def test_function_exists(self):

		divide(8, 6)

	def test_function_returns_correctly(self):

		actual = divide(8, 0)
		expected = 0
		self.assertEqual(actual, expected)

		actual = divide(5, 2)
		expected = 2.5
		self.assertEqual(actual, expected)

	def test_function_raises_exceptions_for_invalid_inputs(self):

		self.assertRaises(TypeError, divide, True)
		self.assertRaises(TypeError, divide, "hello")




class TestFactorFunction(TestCase):

	def test_function_exists(self):

		factor_of(8)

	def test_function_returns_correctly(self):

		actual = factor_of(8)
		expected = 4
		self.assertEqual(actual, expected)

		actual = factor_of(5)
		expected = 2
		self.assertEqual(actual, expected)

	def test_function_raises_exceptions_for_invalid_inputs(self):

		self.assertRaises(TypeError, factor_of, True)
		self.assertRaises(TypeError, factor_of, "hello")
		self.assertRaises(ValueError, factor_of, -6)




class TestIsSquareFunction(TestCase):

	def test_function_exists(self):

		is_square(8)

	def test_function_returns_correctly(self):

		actual = is_square(9)
		expected = True
		self.assertEqual(actual, expected)

		actual = is_square(5)
		expected = False
		self.assertEqual(actual, expected)

	def test_function_raises_exceptions_for_invalid_inputs(self):

		self.assertRaises(TypeError, is_square, True)
		self.assertRaises(TypeError, is_square, "hello")
		self.assertRaises(ValueError, is_square, -12)




class TestIsPalindromeFunction(TestCase):

	def test_function_exists(self):

		is_palindrome(87563)

	def test_function_returns_correctly(self):

		actual = is_palindrome(45655)
		expected = False
		self.assertEqual(actual, expected)

		actual = is_palindrome(96969)
		expected = True
		self.assertEqual(actual, expected)

	def test_function_raises_exceptions_for_invalid_inputs(self):

		self.assertRaises(TypeError, is_palindrome, None)
		self.assertRaises(ValueError, is_palindrome, 125245)
		self.assertRaises(TypeError, is_palindrome, "string")




class TestFactorialFunction(TestCase):

	def test_function_exists(self):

		factorial_of(5)

	def test_function_returns_correctly(self):

		actual = factorial_of(5)
		expected = 120
		self.assertEqual(actual, expected)

		actual = factorial_of(4)
		expected = 24
		self.assertEqual(actual, expected)

	def test_function_raises_exceptions_for_invalid_inputs(self):

		self.assertRaises(TypeError, factorial_of, True)
		self.assertRaises(TypeError, factorial_of, "hello")
		self.assertRaises(ValueError, factorial_of, -6)




class TestSquareOfFunction(TestCase):

	def test_function_exists(self):

		square_of(5)

	def test_function_returns_correctly(self):

		actual = square_of(5)
		expected = 25
		self.assertEqual(actual, expected)

		actual = square_of(4)
		expected = 16
		self.assertEqual(actual, expected)

	def test_function_raises_exceptions_for_invalid_inputs(self):

		self.assertRaises(TypeError, square_of, True)
		self.assertRaises(TypeError, square_of, "hello")



























































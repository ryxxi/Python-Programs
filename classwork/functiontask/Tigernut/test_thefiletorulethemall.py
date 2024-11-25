from unittest import TestCase
from anagramfunction import find_anagram
from vowelfinder import get_vowels
from evensumfunction import get_even_sum
from primefunction import find_prime
from palindromefunction import get_palindrome
from listaveragefunction import get_average
from reversestringfunction import get_reverse
from removespacefunction import remove_space
from mergeandsortfunction import merge_and_sort
from capitalisestringfunction import capitalise


class TestAnagramFunction(TestCase):

	def test_function_exists(self):

		find_anagram("hello", "twelve")

	def test_fuction_returns_true(self):

		actual = find_anagram("hello", "nicely")
		expected = False
		self.assertEqual(actual, expected)

		actual = find_anagram("hia", "iaHH")
		expected = False
		self.assertEqual(actual, expected)

	def test_raises_exception_for_invalid_inputs(self):

		self.assertRaises(TypeError, find_anagram, 12, "hello")
		self.assertRaises(TypeError, find_anagram, True, "yes")


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


class TestPrimeFunction(TestCase):

	def test_function_exists(self):

		find_prime(7)

	def test_function_returns_true(self):

		actual = find_prime(12)
		expected = "Is not prime"
		self.assertEqual(actual, expected)

		actual = find_prime(13)
		expected = "Is prime"
		self.assertEqual(actual, expected)

	def test_function_raises_exception_for_invalid_inputs(self):

		self.assertRaises(TypeError, find_prime, 12.5)
		self.assertRaises(TypeError, find_prime, True)
		self.assertRaises(TypeError, find_prime, "yes")


class TestPalindromFunction(TestCase):

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


from unittest import TestCase
from listaveragefunction import get_average

class TestAverageFunction(TestCase):

	def test_function_exists(self):

		integers = [1, 3, 8, 6, 4]
		get_average(integers)

	def test_fuctions_returns_true(self):

		integers = [1, 2, 3, 4, 5, 6, 7, 8]
		actual = get_average(integers)
		expected = 4.5
		self.assertEqual(actual, expected)

		integers = [1.5, 2.5, 3]
		actual = get_average(integers)
		expected = 7/3
		self.assertEqual(actual, expected)

	def test_function_raises_exception_for_invalid_inputs(self):

		mixed_list = [1.5, 2.5, 3, "hello", True]
		self.assertRaises(TypeError, get_average, mixed_list)


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


class TestRemoveSpaceFunction(TestCase):

	def test_function_exists(self):

		remove_space("hello world")

	def test_fuction_returns_true(self):

		actual = remove_space("hello i am leke")
		expected = "helloiamleke"
		self.assertEqual(actual, expected)

	def test_raises_exception_for_invalid_inputs(self):

		self.assertRaises(TypeError, remove_space, 12,)
		self.assertRaises(TypeError, remove_space, True)


class TestDuplicatesFunction(TestCase):

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


class TestMergeFunction(TestCase):

	def test_that_get_sum_of_odd_function_works(self):
		merge_and_sort([1, 2, 3], [4, 5])
        
	def test_that_get_merge_list_returns_correct_value(self):
		list1 = [-12, 71, 34, 29]
		list2 = [7, 1, 2, 3]
		actual = merge_and_sort(list1, list2)
		expected = [-12, 1, 2, 3, 7, 29, 34, 71]
		self.assertEqual(actual, expected)
        
	def test_that_get_merge_list_is_string(self):
		self.assertRaises(TypeError, merge_and_sort, "hello") 


class TestCapitaliseFunction(TestCase):

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































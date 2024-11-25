from unittest import TestCase
from allfunctions import get_largest_element
from allfunctions import get_reverse
from allfunctions import check_for
from allfunctions import get_odd_indices
from allfunctions import get_even_indices
from allfunctions import get_running_total
from allfunctions import check_if_palindrome
from allfunctions import for_loop_sum
from allfunctions import while_loop_sum
from allfunctions import concatenate_lists
from allfunctions import alternate_lists
from allfunctions import make_list

class TestLargestElementFunction(TestCase):

	def test_function_exists(self):

		example = [1,2,3,4]
		get_largest_element(example)

	def test_returns_correctly(self):

		example = [1,2,3,4]
		actual = get_largest_element(example)
		expected = 4
		self.assertEqual(actual, expected)

		example = [5.65,2,9.1,4]
		actual = get_largest_element(example)
		expected = 9.1
		self.assertEqual(actual, expected)

	def test_raises_exception_with_invalid_inputs(self):

		self.assertRaises(TypeError, get_largest_element, None)
		self.assertRaises(TypeError, get_largest_element, [2, True, 7.99, "hello"]) 
		self.assertRaises(TypeError, get_largest_element, "hello")




class TestReverseList(TestCase):

	def test_function_exists(self):

		example = [1,2,3,4]
		get_reverse(example)

	def test_returns_correctly(self):

		example = [1, 2, 3, 4]
		actual = get_reverse(example)
		expected = example.reverse()
		self.assertEqual(actual, expected)

		example = [3, "hello", "nice"]
		actual = get_reverse(example)
		expected = example.reverse()
		self.assertEqual(actual, expected)

	def test_raises_exception_with_invalid_inputs(self):

		self.assertRaises(TypeError, get_reverse, None)
		self.assertRaises(TypeError, get_reverse, "hello")





class TestCheckForElementFunction(TestCase):

	def test_function_exists(self):

		example = [True, 2, "hello", 4]
		check_for(example, 5)

	def test_function_returns_correctly(self):

		example = [False, "Yes", "12", 4]
		actual = check_for(example, 4)
		expected = True
		self.assertEqual(actual, expected)

		actual = check_for(example, 8)
		expected = False
		self.assertEqual(actual, expected)

	def test_function_raises_exception_for_invalid_inputs(self):

		numbers = [1, 2, 3, 4]
		self.assertRaises(TypeError, check_for, 12)
		self.assertRaises(TypeError, check_for, None)
		self.assertRaises(TypeError, check_for, numbers)






class TestOddIndexElementsFunction(TestCase):

	def test_function_exists(self):

		example = [2, "nice", "clue", True, 4.1]
		get_odd_indices(example)

	def test_function_returns_correctly(self):

		example = [2, "nice", "clue", True, 4.1]
		actual = get_odd_indices(example)
		expected = ["nice", True]
		self.assertEqual(actual, expected)

	def test_function_raises_exceptions_for_invalid_inputs(self):

		self.assertRaises(TypeError, get_odd_indices, None)
		self.assertRaises(TypeError, get_odd_indices, 12)
		self.assertRaises(TypeError, get_odd_indices, True, "yes")





class TestEvenIndexElementsFunction(TestCase):

	def test_function_exists(self):

		example = [2, "nice", "clue", True, 4.1]
		get_even_indices(example)

	def test_function_returns_correctly(self):

		example = [2, "nice", "clue", True, 4.1]
		actual = get_even_indices(example)
		expected = [2, "clue", 4.1]
		self.assertEqual(actual, expected)

	def test_function_raises_exceptions_for_invalid_inputs(self):

		self.assertRaises(TypeError, get_even_indices, None)
		self.assertRaises(TypeError, get_even_indices, 12)
		self.assertRaises(TypeError, get_even_indices, True, "yes")




class TestRunningTotalFunction(TestCase):

	def test_function_exists(self):

		example = [1, 2, 3, 4]
		get_running_total(example)

	def test_function_returns_correctly(self):

		example = [1, 2, 3, 4]
		actual = get_running_total(example)
		expected = [1, 3, 6, 10]
		self.assertEqual(actual, expected)

		example = [1, 3, 5, 7, 9]
		actual = get_running_total(example)
		expected = [1, 4, 9, 16, 25]
		self.assertEqual(actual, expected)

	def test_function_raises_exceptions_for_invalid_inputs(self):

		self.assertRaises(TypeError, get_running_total, None)
		self.assertRaises(TypeError, get_running_total, True)
		self.assertRaises(TypeError, get_running_total, [1, 3, "hello"])




class TestCheckPalindromeFunction(TestCase):

	def test_function_exists(self):

		check_if_palindrome("hello")

	def test_function_returns_correctly(self):

		actual = check_if_palindrome("nice")
		expected = False
		self.assertEqual(actual, expected)

		actual = check_if_palindrome("madam")
		expected = True
		self.assertEqual(actual, expected)

	def test_function_raises_exceptions_for_invalid_inputs(self):

		self.assertRaises(TypeError, check_if_palindrome, None)
		self.assertRaises(TypeError, check_if_palindrome, 12)
		self.assertRaises(TypeError, check_if_palindrome, "string", 3)




class TestForLoopSum(TestCase):

	
	def test_function_exists(self):

		example = [1, 2, 3, 4]
		for_loop_sum(example)

	def test_function_returns_correctly(self):

		example = [1, 2, 3, 4]
		actual = for_loop_sum(example)
		expected = 10
		self.assertEqual(actual, expected)

		example = [1, 3, 5, 7, 9]
		actual = for_loop_sum(example)
		expected = 25
		self.assertEqual(actual, expected)

	def test_function_raises_exceptions_for_invalid_inputs(self):

		self.assertRaises(TypeError, for_loop_sum, None)
		self.assertRaises(TypeError, for_loop_sum, True)
		self.assertRaises(TypeError, for_loop_sum, [1, 3, "hello"])




class TestWhileLoopSum(TestCase):

	
	def test_function_exists(self):

		example = [1, 2, 3, 4]
		while_loop_sum(example)

	def test_function_returns_correctly(self):

		example = [1, 2, 3, 4]
		actual = while_loop_sum(example)
		expected = 10
		self.assertEqual(actual, expected)

		example = [1, 3, 5, 7, 9]
		actual = while_loop_sum(example)
		expected = 25
		self.assertEqual(actual, expected)

	def test_function_raises_exceptions_for_invalid_inputs(self):

		self.assertRaises(TypeError, while_loop_sum, None)
		self.assertRaises(TypeError, while_loop_sum, True)
		self.assertRaises(TypeError, while_loop_sum, [1, 3, "hello"])




class TestConcatenateLists(TestCase):

	
	def test_function_exists(self):

		list1 = [1, 2, 3, 4]
		list2 = [5, 6, 7]
		concatenate_lists(list1, list2)

	def test_function_returns_correctly(self):

		list1 = [1, 2, 3, 4]
		list2 = [5, 6, 7]
		actual = concatenate_lists(list1, list2)
		expected = [1, 2, 3, 4, 5, 6, 7]
		self.assertEqual(actual, expected)

	def test_function_raises_exceptions_for_invalid_inputs(self):

		self.assertRaises(TypeError, concatenate_lists, None)
		self.assertRaises(TypeError, concatenate_lists, [2, 5, 7, 9], 12)
		self.assertRaises(TypeError, concatenate_lists, [1, 3, "hello"])




class AlternateLists(TestCase):

	def test_function_exists(self):

		list1 = [1, 2, 3, 4]
		list2 = [5, 6, 7]
		alternate_lists(list1, list2)

	def test_function_returns_correctly(self):

		list1 = [1, 2, 3, 4]
		list2 = [5, 6, 7]
		actual = alternate_lists(list1, list2)
		expected = [1, 5, 2, 6, 3, 7, 4]
		self.assertEqual(actual, expected)

	def test_function_raises_exceptions_for_invalid_inputs(self):

		self.assertRaises(TypeError, alternate_lists, None)
		self.assertRaises(TypeError, alternate_lists, [2, 5, 7, 9], 12)
		self.assertRaises(TypeError, alternate_lists, [1, 3, "hello"])




class NumberToList(TestCase):

	def test_function_exists(self):

		make_list(24)

	def test_function_returns_correctly(self):

		actual = make_list(2575)
		expected = [2, 5, 7, 5]
		self.assertEqual(actual, expected)

		actual = make_list(43.564)
		expected = [4, 3, ".", 5, 6, 4]
		self.assertEqual(actual, expected)

	def test_fucntion_raises_exceptions_for_invalid_inputs(self):

		self.assertRaises(TypeError, make_list, None)
		self.assertRaises(TypeError, make_list, "Hello")
		self.assertRaises(TypeError, make_list, False)





































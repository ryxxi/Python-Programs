from unittest import TestCase
from mergeandsortfunction import merge_and_sort

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
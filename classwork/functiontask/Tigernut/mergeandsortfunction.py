def merge_and_sort(list1, list2):
	
	if isinstance(list1, list) and isinstance(list2, list):

		new = list1 + list2

		new = sorted(new)

		return new

list1 = [-12, 71, 34, 29]
list2 = [7, 1, 2, 3]
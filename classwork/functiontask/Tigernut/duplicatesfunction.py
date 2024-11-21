def check_duplicates(list1, list2):

	for value1 in list1:

		for value2 in list2:

			if value1 == value2:

				return True

		return False
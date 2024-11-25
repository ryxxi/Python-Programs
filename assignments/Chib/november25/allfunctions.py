def get_largest_element(numbers):

	if isinstance(numbers, list):

		largest = numbers[0]

		for number in numbers:

			if isinstance(number, (float, int)):

				if number > largest: largest = number

			else: raise TypeError

		return largest

	raise TypeError




def get_reverse(original_list):

	if isinstance(original_list, list):

		new_list = original_list.reverse()

		return new_list

	raise TypeError




def check_for(collection, value):

	isPresent = False

	if isinstance(collection, list):

		for element in collection:

			if element == value:

				isPresent = True

		return isPresent

	raise TypeError




def get_odd_indices(original_list):

	if isinstance(original_list, list):
	
		length = len(original_list)
		new_list = []

		for count in range(1, length, 2):

			new_list.append(original_list[count])

		return new_list

	raise TypeError




def get_even_indices(original_list):

	if isinstance(original_list, list):
	
		length = len(original_list)
		new_list = []

		for count in range(0, length, 2):

			new_list.append(original_list[count])

		return new_list

	raise TypeError





def get_running_total(original_list):

	if isinstance(original_list, list):

		new_list = []
		total = 0

		for value in original_list:

			if isinstance(value, (int, float)):

				total += value
				new_list.append(total)

			else: raise TypeError

		return new_list

	raise TypeError





def check_if_palindrome(string):

	if isinstance(string, str):

		reverse = string[::-1]
		isPalindrome = False

		if reverse == string: isPalindrome = True

		return isPalindrome

	raise TypeError





def for_loop_sum(original_list):

	if isinstance(original_list, list):

		total = 0

		for value in original_list:

			if isinstance(value, (int, float)):

				total += value

			else: raise TypeError

		return total

	raise TypeError





def while_loop_sum(example_list):

	if isinstance(example_list, list):

		total = 0
		count = 0

		while count < len(example_list):

			if isinstance(example_list[count], (int, float)):

				total += example_list[count]
				count += 1

			else: raise TypeError

		return total

	raise TypeError




def concatenate_lists(list1, list2):

	if isinstance(list1, list) and isinstance(list2, list):

		return list1 + list2

	raise TypeError



def alternate_lists(list1, list2):

	if isinstance(list1, list) and isinstance(list2, list):

		new_list = []
		i = 0
		j = 0

		while i < len(list1) and j < len(list2):

			new_list.append(list1[i])
			new_list.append(list2[j])
			i += 1
			j += 1

		while i < len(list1):

			new_list.append(list1[i])
			i += 1

		while j < len(list2):

			new_list.append(list2[j])
			j += 1

		return new_list

	raise TypeError




def make_list(number):

	if isinstance(number, (int, float)) and not isinstance(number, bool):

		number = str(number)
		new_list = []

		for char in number:

			if char.isdigit():

				char = int(char)
				new_list.append(char)

			else:

				new_list.append(char)

		return new_list

	raise TypeError













































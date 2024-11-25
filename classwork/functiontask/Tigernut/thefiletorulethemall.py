def find_anagram(string1, string2):

	if type(string1) is str and type(string2) is str:

		string1 = string1.lower()
		string2 = string2.lower()

		if sorted(string1) == sorted(string2):

			return True

		else: return False

	else: raise TypeError


def get_vowels(string):

	vowels = "AEIOUaeiou"
	vowel_counter = 0

	if type(string) is str:

		for char in string:
			if char in vowels:
				vowel_counter += 1

	else: raise TypeError

	return vowel_counter


def get_even_sum(integers):

	total = 0
	for value in integers:

		if type(value) in [int, float]:
	
			if value % 2 == 0:

				total += value

		else: continue

	return total


def find_prime(number):

	if type(number) is int:

		for divider in range(2, number):

			if number % divider == 0:

				return "Is not prime"

			else: return "Is prime"

	else: raise TypeError


def get_average(numbers):

	total = 0
	for value in numbers:

		if type(value) not in [int, float]:

			raise TypeError

		else:

			total += value

	return total / len(numbers)


def get_reverse(string):

	if type(string) is str:

		return string[::-1]

	else: raise TypeError


def remove_space(anything):

	if isinstance(anything, str):
		new = anything.replace(" ", "")

		return new

	raise TypeError


def check_duplicates(list1, list2):

	for value1 in list1:

		for value2 in list2:

			if value1 == value2:

				return True

		return False


def merge_and_sort(list1, list2):
	
	if isinstance(list1, list) and isinstance(list2, list):

		new = list1 + list2

		new = sorted(new)

		return new


def capitalise(string):

	if isinstance(string, list):

		for value in string:

			if isinstance(value, str):

				continue

			else: raise TypeError

		return [s[0].upper() + s[1::] for s in string if isinstance(s, str)]
	
	raise TypeError

		

		
def odd_even_list(numbers):

	odds = 0
	evens = 0

	if isinstance(numbers, list):

		for number in numbers:

			if isinstance(number, int):

				if number % 2 == 0: evens += 1
				else: odds += 1

			else: raise TypeError

		return [odds, evens]

	else: raise TypeError


print(odd_even_list([5,4,3,2,1,21]))
def get_average(numbers):

	total = 0
	for value in numbers:

		if type(value) not in [int, float]:

			raise TypeError

		else:

			total += value

	return total / len(numbers)
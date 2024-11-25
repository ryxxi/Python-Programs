def get_sum(numbers):


	total = 0
	single_total = 0

	for value in numbers:

		single_total += value

	total = single_total * (len(numbers) - 1)

	return total

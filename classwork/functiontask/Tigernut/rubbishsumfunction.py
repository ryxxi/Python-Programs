def get_sum(numbers):


	total = 0
	single_total = 0

	for value in numbers:

		single_total += value

	total = single_total * (len(numbers) - 1)

	return total
	
	

numbs = [1, 2, 3, 4, 5, 7, 5, 3]

print(get_sum(numbs))
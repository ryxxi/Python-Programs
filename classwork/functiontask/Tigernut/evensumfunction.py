def get_even_sum(integers):

	total = 0
	for value in integers:

		if type(value) in [int, float]:
	
			if value % 2 == 0:

				total += value

		else: continue

	return total
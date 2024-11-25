def get_product(numbers):

	product = 1
	if isinstance(numbers, list):

		for value in numbers:

			if isinstance(value, (float, int)):

				product *= value

			else: raise TypeError

		return product

	raise TypeError
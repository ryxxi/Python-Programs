def get_root_or_remainder(number):

	if number >= 0:
		if number % 5 == 0:
			return number ** 0.5

		else:
			return number % 5

	elif number < 0:
		if number % 5 == 0:
			raise ValueError

		else:
			return number % 5

	raise TypeError
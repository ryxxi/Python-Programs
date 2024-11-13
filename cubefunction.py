def get_cube(number):

	if type(number) is int:
		return number ** 3

	elif type(number) is float:
		return round((number ** 3), 3)

	raise TypeError
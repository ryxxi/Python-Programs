def remove_space(anything):

	if isinstance(anything, str):
		new = anything.replace(" ", "")

		return new

	raise TypeError
def get_floats(input1, input2):

	if type(input1) is float and type(input2) is float:
		return 2

	elif type(input1) is float and type(input2) is not float:
		return 1

	elif type(input1) is not float and type(input2) is float:
		return 1

	else:
		return 0
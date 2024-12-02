def cube_list(example_list):

	return [x ** 3 for x in example_list]	

def make_list():

	return cube_list([x for x in range(1, 6)])

print(make_list())
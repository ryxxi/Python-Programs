def get_even_count(example_list):

	return sum(1 for x in example_list if x % 2 == 0)

print(get_even_count([1,2,3,4,5]))
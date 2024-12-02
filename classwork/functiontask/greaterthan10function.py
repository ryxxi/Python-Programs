def greater_than_ten(a_list):

	return list(filter(lambda x: x >10, a_list))

print(greater_than_ten([1,9,8,7,99,88,77,66,55]))
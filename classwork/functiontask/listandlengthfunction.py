def get_strings_with_length(example_list, number):

	return list(filter(lambda x: len(x) >= number, example_list))

print(get_strings_with_length(["hello", "nice", "bless", "play"], 4))
def check_list_palindromes(string_list):

	return list(map(lambda x: x == x[::-1], string_list))


strings = ["hello", "madam", "lifefil", "polly", 121]
print(check_list_palindromes(strings))
def filter_vowels(string):

	vowels = "aeiouAEIOU"
	return list(filter(lambda x: x in vowels, string))

string = "hello world divine is a stupid dickhead"
print(filter_vowels(string))
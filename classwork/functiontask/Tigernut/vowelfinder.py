def get_vowels(string):

	vowels = "AEIOUaeiou"
	vowel_counter = 0

	if type(string) is str:

		for char in string:
			if char in vowels:
				vowel_counter += 1

	else: raise TypeError

	return vowel_counter
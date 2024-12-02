def remove_vowels_from_strings(strings: list):

	vowels = "aeiouAEIOU"

	return list(filter(lambda x: x not in vowels, strings[1]))

print(remove_vowels_from_strings(["hello", "goodbye", "well done"]))
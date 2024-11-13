def vowel_finder(string):

	vowels = "AEIOUaeiou"
	vowel_counter = 0

	for char in string:
		if char in vowels:
			vowel_counter += 1

	return vowel_counter


string = input("Enter a message: ")

print(vowel_finder(string))
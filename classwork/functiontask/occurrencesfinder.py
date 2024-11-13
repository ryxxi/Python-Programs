def occurrence_finder(string1, string2):

	occurrence_counter = 0

	for char in string2:
		if char == string1: occurrence_counter += 1
	return occurrence_counter

word = input("Enter anything: ")
letter = input("Enter a letter to see how many times that letter appears: ")

print(occurrence_finder(letter, word))
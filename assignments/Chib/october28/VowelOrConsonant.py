input = input("Enter a single letter: ")

if (len(input) == 1) and (input.isalpha() == True):
	letter = input.capitalize()

	if (letter == "A") or (letter == "E") or (letter == "I") or (letter == "O") or (letter == "U"):
		print("Vowel")

	else:
		print("Consonant")

else:
	print("Error")
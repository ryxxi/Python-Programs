def create_acronym(string):

	words = string.split()
	acronym = "".join(letter[0].upper() for letter in words)
	return acronym

string = input("Enter anything: ")
print(create_acronym(string))
			
def find_anagram(string1, string2):

	if type(string1) is str and type(string2) is str:

		string1 = string1.lower()
		string2 = string2.lower()

		if sorted(string1) == sorted(string2):

			return True

		else: return False

	else: raise TypeError
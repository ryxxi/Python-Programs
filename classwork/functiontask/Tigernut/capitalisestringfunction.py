def capitalise(string):

	if isinstance(string, list):

		for value in string:

			if isinstance(value, str):

				continue

			else: raise TypeError

		return [s[0].upper() + s[1::] for s in string if isinstance(s, str)]
	
	raise TypeError
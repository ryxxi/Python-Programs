def capitalise(string):

	if isinstance(string, list):

		try:

			return [s[0].upper() + s[1::] for s in string if isinstance(s, str)]

		except TypeError:
	
			raise TypeError

	
	raise TypeError
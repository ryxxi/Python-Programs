def get_palindrome(string):

	if type(string) is str:

		is_palindrome = False
		reverse = string[::-1]
		if string == reverse: is_palindrome = True

		return is_palindrome

	else: raise TypeError

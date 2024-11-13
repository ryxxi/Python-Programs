def palindrome_checker(string):

	is_palindrome = False
	reverse = string[::-1]
	if string == reverse: is_palindrome = True

	return is_palindrome

word = input("Enter a word to see if it's a palindrome: ")

print(palindrome_checker(word))

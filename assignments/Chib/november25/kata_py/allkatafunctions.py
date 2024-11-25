def is_even(number):

	if isinstance(number, int) and not isinstance(number, bool):

		is_even = False

		if number % 2 ==0: is_even = True

		return is_even

	raise TypeError




def is_prime(number):

	if isinstance(number, int) and not isinstance(number, bool):

		is_prime = True

		for divider in range(2, number):

			if number % divider == 0: is_prime = False

		return is_prime

	raise TypeError




def subtract(number1, number2):

	if isinstance(number1, int) and isinstance(number2, int) and not isinstance(number1, bool) and not isinstance(number2, bool):

		result = abs(number1 - number2)

		return result

	raise TypeError




def divide(number1, number2):

	if isinstance(number1, int) and isinstance(number2, int) and not isinstance(number1, bool) and not isinstance(number2, bool):

		if number2 == 0: return 0

		result = float(number1 / number2)

		return result

	raise TypeError




def factor_of(number):

	if isinstance(number, int) and not isinstance(number, bool):

		if number < 0: raise ValueError

		else:

			factor_count = 0

			for divider in range(1, number + 1):

				if number % divider == 0: factor_count += 1

			return factor_count

	raise TypeError




def is_square(number):

	if isinstance(number, int) and not isinstance(number, bool):

		is_square = False

		if number < 0: raise ValueError

		elif (number ** 0.5) % 1 == 0: is_square = True

		return is_square

	raise TypeError




def is_palindrome(number):

	if isinstance(number, int) and not isinstance(number, bool):

		string = str(number)
		length = len(string)

		if length == 5:
			is_palindrome = False
			reverse = string[::-1]

			if reverse == string: is_palindrome = True

			return is_palindrome

		else: raise ValueError

	raise TypeError




def factorial_of(number):

	if isinstance(number, int) and not isinstance(number, bool):

		if number == 0: return 1

		elif number > 0:
			factorial = 1

			for number in range(1, number + 1):

				factorial *= number

			return factorial

		else: raise ValueError

	raise TypeError




def square_of(number):

	if isinstance(number, int) and not isinstance(number, bool):

		return number ** 2

	raise TypeError






























































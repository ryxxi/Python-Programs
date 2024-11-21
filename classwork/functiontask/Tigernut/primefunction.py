def find_prime(number):

	if type(number) is int:

		for divider in range(2, number):

			if number % divider == 0:

				return "Is not prime"

			else: return "Is prime"

	else: raise TypeError
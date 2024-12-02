def get_primes_before(number):

	return[

		divider
		for divider in range(2, number)
		if all(divider % check_divider != 0 for check_divider in range(2, divider))

	]

print(get_primes_before(19))
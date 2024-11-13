def prime_check(number):

	result = 0
	max_divider = number ** 0.5

	prime = True

	if number <= 1:
		return false

	for count in range (2, int (max_divider)):
		result = number % count
		if result == 0:
			return prime = False
		else:
			return prime = True
	return prime




number = int(input("Enter a number: "))

print(prime_check(number))
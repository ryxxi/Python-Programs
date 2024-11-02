number = input("Enter a positive 5 digit integer: ")

if number.isdigit():
	number = int(number)
	if number < 100000 and number > 0:
		first_digit = number // 10000
		second_digit = (number // 1000) % 10
		fourth_digit = (number // 10) % 10
		fifth_digit = number % 10

		if first_digit == fifth_digit and second_digit == fourth_digit:
			print(f"\n{number} is a palindrome\n")

		else:
			print(f"\n{number} is not a palindrome\n")

else:
	number = float(number)
	print(f"\n{number} is not a positive 5 digit integer\n")
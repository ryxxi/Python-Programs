number = input("Enter a positive 3 digit integer: ")

if number.isdigit():
	number = int(number)
	if number < 1000 and number > 0:
		first_digit = number // 100
		third_digit = number % 10

		if first_digit == third_digit:
			print(f"{number} is a palindrome")

		else:
			print(f"\n{number} is not a palindrome\n")

else:
	number = float(number)
	print(f"\n{number} is not a positive 3 digit integer\n")
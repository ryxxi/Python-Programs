number = int(input("Enter an integer between 0 and 1000: "))

if (number < 1000 and number > 0):
	first_digit = number // 100
	second_digit = number // 10 % 10
	third_digit = number % 10

	sum = first_digit + second_digit + third_digit

	print(f"The sum of {number}'s digits is {sum}")

else:
	print("The number entered does not lie within the stated parameters")
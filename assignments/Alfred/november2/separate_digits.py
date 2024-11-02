number = int(input("Enter a 5 digit integer: "))
divider = 10000

while number > 0:
	digit = number // divider
	print(digit, end=" ")
	number = number % divider
	divider //= 10
print()
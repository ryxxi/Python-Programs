number = int(input("Enter a number: "))
factorial = number
original = number

while number != 1:
	factorial*=(number-1)
	number-=1
print(f"\nThe factorial of {original} is {factorial}\n")
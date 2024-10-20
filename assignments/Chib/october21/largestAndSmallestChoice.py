number = input("Enter a number, enter -1 to end the program: ")
number = int(number)

largest = -(9 ** 9)
smallest = 9 ** 9

while (number != -1):
	if (number < smallest):
		smallest = number

	if (number > largest):
		largest = number
	
	number = input("Enter a number, enter -1 to end the program: ")
	number = int(number)

print(f"From all input values, the smallest is {smallest} and the largest is {largest}")
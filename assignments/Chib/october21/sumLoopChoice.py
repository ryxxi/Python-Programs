number1 = input("Enter a number: ")
number1 = int(number1)
number2 = input("Enter a number: ")
number2 = int(number2)

result = number1 + number2

print(f"{number1} + {number2} = {result}")

answer = input("Would you like to repeat this program?(Y/N): ")

while (answer == "Y"):
	number1 = input("Enter a number")
	number1 = int(number1)
	number2 = input("Enter a number")
	number2 = int(number2)

	result = number1 + number2

	print(f"{number1} + {number2} = {result}")

	answer = input("Would you like to repeat this program?(Y/N): ")
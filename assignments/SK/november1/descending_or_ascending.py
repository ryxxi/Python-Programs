number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))

if number1 < number2 and number2 < number3:
	print("Numbers are in ascending order")
elif number1 > number2 and number2 > number3:
	print("Numbers are in descending order")
else:
	print("Numbers are in neither ascending nor descending order")
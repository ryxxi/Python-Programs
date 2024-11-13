def multiple_function(number1, number2):

	sum = 0

	for number in range (number1, number2, number1):
		sum += number	
	return sum

number = int(input("Enter an integer: "))
number2 = int(input("Enter an integer: "))

print(multiple_function(number, number2))
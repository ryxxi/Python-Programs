import sys

def functionfuckery(number1, number2, file=sys.stdout) :

	sum = number1 + number2

	file.write(str(sum) + "\n")
	return sum

number1 = 67
number2 = 33

functionfuckery(number1, number2)
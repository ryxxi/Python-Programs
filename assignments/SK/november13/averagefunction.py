def get_average(number1, *numbers):

	return (sum(numbers) + number1) / (len(numbers) + 1)


number1 = 12
number2 = 12
number3 = 6
number4 = 8
number5 = 2
number6 = 10

print(get_average(number1, number2, number3, number4, number5))
def even_sum(number):

	sum = 0

	for number in range (number, 0, -1):
		if number % 2 == 0: 
			sum += number	
	return sum

number = int(input("Enter an integer: "))

print(even_sum(number))
def even_checker(number):

	even_counter = 0

	for number in range (number, 0, -1):

		if number % 2 == 0: 
			even_counter +=1
			
	return even_counter

number = int(input("Enter an integer: "))

print(even_checker(number))
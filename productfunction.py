def get_product(num1, num2): 
	
	positive = (num1 >= 0 and num2 >= 0) or (num1 < 0 and num2 < 0)

	if type(num1) is int and type(num2) is int:

		num1 = abs(num1)
		num2 = abs(num2)

		product = 0

		for _ in range(num2):
			product += num1

		if positive == False:
			product = -product

		return product
	

	if type(num1) is int and type(num2) is float:

		num1 = abs(num1)
		num2 = abs(num2)

		product = 0

		for _ in range(num1):
			product += num2

		if positive == False:
			product = -product

		return product

	if type(num1) is float and type(num2) is int:

		num1 = abs(num1)
		num2 = abs(num2)

		product = 0

		for _ in range(num2):
			product += num1

		if positive == False:
			product = -product

		return product

	if type(num1) is float and type(num2) is float:

		num1 = abs(num1)
		num2 = abs(num2)

		integer_of_num1 = int(num1)
		decimal_of_num1 = num1 - integer_of_num1

		product = 0

		for _ in range(integer_of_num1):
			product += num2

		increment = num2 / 10
		fraction = 0

		while decimal_of_num1 > 0:
			if decimal_of_num1 >= 0.1:
				fraction += increment
				decimal_of_num1 -= 0.1
			else:
				increment /= 10

		product += fraction

		if positive == False:
			product = -product

		return product


































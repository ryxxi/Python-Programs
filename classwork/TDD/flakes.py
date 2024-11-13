def get_discount(original_price, discount):

	if type(original_price) in [float, int] and type(discount) in [float, int]:
	
		if original_price >= 0 and discount >= 0:
			discounted_price = original_price * ((100 - discount) / 100)
			return round(discounted_price, 2)
		else:
			raise ValueError

	raise TypeError


def get_floats(input1, input2):

	if type(input1) is float and type(input2) is float:
		return 2

	elif type(input1) is float and type(input2) is not float:
		return 1

	elif type(input1) is not float and type(input2) is float:
		return 1

	else:
		return 0


def get_future_investment_value(principal, monthly_interest, years):
	
	if type(principal) in [int, float] and type(monthly_interest) in [int, float] and type(years) in [int, float]:
		if principal > 0 and years > 0:
			future_investment_value = principal * ((1 + (monthly_interest / 100)) ** (years * 12))
			return round(future_investment_value, 2)

		elif principal < 0 or years < 0:
			raise ValueError

	raise TypeError


def get_root_or_remainder(number):

	if type(number) in [float, int]:
		if number >= 0:
			if number % 5 == 0:
				return number ** 0.5
	
			else:
				return number % 5

		elif number < 0:
			if number % 5 == 0:
				raise ValueError

			else:
				return number % 5
	
	raise TypeError
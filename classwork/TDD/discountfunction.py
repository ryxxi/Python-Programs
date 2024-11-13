def get_discount(original_price, discount):

	if type(original_price) in [float, int] and type(discount) in [float, int]:
	
		if original_price >= 0 and discount >= 0:
			discounted_price = original_price * ((100 - discount) / 100)
			return round(discounted_price, 2)
		else:
			raise ValueError

	raise TypeError
def get_future_investment_value(principal, monthly_interest, years):
	
	if type(principal) in [int, float] and type(monthly_interest) in [int, float] and type(years) in [int, float]:
		if principal > 0 and years > 0:
			future_investment_value = principal * ((1 + (monthly_interest / 100)) ** (years * 12))
			return round(future_investment_value, 2)

		elif principal < 0 or years < 0:
			raise ValueError

	raise TypeError
numerator = 1
denominator = 1
factorial = denominator
original_denominator = denominator
fraction = numerator / factorial

e = 1

counter = 50

while counter > 0:

	while denominator != 1 :
		factorial *= (denominator - 1)
		denominator -= 1
	
	fraction = numerator / factorial
	e += fraction

	original_denominator += 1
	denominator = original_denominator
	factorial = denominator

	counter -=1

print(e)
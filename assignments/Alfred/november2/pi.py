numerator = -4
denominator = 3
fraction = numerator / denominator

pi = 4

counter = 100

while counter > 0:

	pi += fraction

	denominator +=2
	numerator *= -1
	fraction = numerator / denominator
	counter -=1

print(pi)
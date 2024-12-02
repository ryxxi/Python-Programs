def digit_sum(number):

	return sum(list(map(lambda x: int(x),filter(lambda x: x.isdigit(), str(number)))))

print(digit_sum(192374))
counter = 0
pos_counter = 0
neg_counter = 0
zero_counter = 0

while counter < 5:
	number = float(input("Enter a number: "))
	if number == 0:
		zero_counter +=1

	elif number < 0:
		neg_counter +=1

	else:
		pos_counter +=1
	
	counter +=1

print(f"""

Positives: {pos_counter}
Negatives: {neg_counter}
Zeros: {zero_counter}
""")
	
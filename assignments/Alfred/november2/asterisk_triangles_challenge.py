pattern_choice = input("Enter a pattern choice (a, b, c, d): ")

for rows in range (10)
	for row_number in range (rows)
		







for height in range (1, 11):
	for asterisk in range (height):
		print("*", end="")
	print()

for height in range (11, 1, -1):
	for asterisk in range (height - 1):
		print("*", end="")

	print()

for height in range (11, 1, -1):
	for space in range (11-height, ):
		print(" ", end="")
	for asterisk in range(height-1):
		print("*", end="")

	print()

for height in range (1, 11):
	for space in range (10-height, ):
		print(" ", end="")
	for asterisk in range(height):
		print("*", end="")
	print()
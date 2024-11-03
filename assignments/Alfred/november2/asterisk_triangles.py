pattern_choice = input("Enter a pattern choice (a, b, c, d): ")

if pattern_choice == 'a':
	for height in range (1, 11):
		for asterisk in range (height):
			print("*", end="")
		print()

elif pattern_choice == 'b':
	for height in range (11, 1, -1):
		for asterisk in range (height - 1):
			print("*", end="")

		print()

elif pattern_choice == 'c':
	for height in range (11, 1, -1):
		for space in range (11-height, ):
			print(" ", end="")
		for asterisk in range(height-1):
			print("*", end="")

		print()

elif pattern_choice == 'd':
	for height in range (1, 11):
		for space in range (10-height, ):
			print(" ", end="")
		for asterisk in range(height):
			print("*", end="")

		print()
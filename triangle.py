size = int(input("Enter triangle size: "))

for space in range (1, size + 1):
	for triangle in range (1, space + 1):
		print("*", end="")
	print()
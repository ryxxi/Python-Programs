size = int(input("Enter the pyramid's size: "))

for number in range (1, size + 1):
	print(" " * (size - number), f"{number}", end="")
size = int(input("Enter the size of the rhombus: "))

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(0, size+1):
	for j in range(size):
		print(" ", end="")
	for k in range(0, i+1, 1):
		print(letters[i], end="")
	i = 0

	print("")
	
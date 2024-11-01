size = int(input("Enter the size of the rhombus: "))

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(1, size+1):
	for j in range(size - i):
		print(" ", end="")
	print(letters[:i], end="")
	print(letters[i-2::-1])

	
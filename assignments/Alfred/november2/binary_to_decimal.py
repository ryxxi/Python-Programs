binary = input("Enter a binary number: ")
binary_reverse = binary [::-1]
decimal = 0
multiple = 1

for x in binary_reverse:
	x = int(x)
	decimal += (x * multiple)
	multiple *= 2

print(f"The decimal equivalent of binary {binary} is {decimal}")
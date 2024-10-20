print("a	b	pow(a, b)")

a = 1
b = 2
result = a ** b
counter = 0

while (counter < 5):
	print(f"{a}	{b}	{result}")
	a += 1
	b += 1
	result = a ** b
	counter += 1
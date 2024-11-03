number = input("Enter an integer: ")
sum = 0
y = 0

for x in number:
	y = int(x)
	if y >= 5:
		y = 1
	else:
		y = 0
	sum+=y

print(f"\n{sum}\n")
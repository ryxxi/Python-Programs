sum = 0
newNumber = 0

for number in range(4, 9, 4):

	newNumber = number + (number**2)+(number**3)+(number**4)+(number**5)
	sum += newNumber

sum = sum ** 2

print(sum)
number = 4
sum = 0
newNumber = 0

while number <= 10:

	newNumber = number + (number**2) + (number**3) + (number**4) + (number**5)
	sum += newNumber
	number +=4

print(sum)
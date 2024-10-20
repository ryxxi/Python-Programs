negativeCounter = 0
positiveCounter = 0
zeroCounter = 0
numberCounter = 0

while numberCounter < 5:
	number = input("Enter a number: ")
	number = int(number)
	if number < 0:
		negativeCounter +=1
	elif number == 0:
		zeroCounter +=1
	else:
		positiveCounter +=1

	numberCounter +=1

negativeCounter = str(negativeCounter)
positiveCounter = str(positiveCounter)
zeroCounter = str(zeroCounter)

print(f"There is/are {negativeCounter} negative numbers")
print(f"There is/are {positiveCounter} positive numbers")
print(f"There is/are {zeroCounter} zeros")
number = input("Enter a 3 digit number: ")

number = int(number)

digit1 = number // 100
digit2 = (number // 10) % 10
digit3 = number % 10

evenCounter = 0
oddCounter = 0

nature1 = digit1 % 2
nature2 = digit2 % 2
nature3 = digit3 % 2

if nature1 == 0:
	evenCounter = evenCounter + 1
else:
	oddCounter = oddCounter + 1

if nature2 == 0:
	evenCounter = evenCounter + 1
else:
	oddCounter = oddCounter + 1

if nature3 == 0:
	evenCounter = evenCounter + 1
else:
	oddCounter = oddCounter + 1



digit1 = str(digit1)
digit2 = str(digit2)
digit3 = str(digit3)

evenCounter = str(evenCounter)
oddCounter = str(oddCounter)



print(digit3 + "\t" + digit2 + "\t" + digit1)
print("There are " + evenCounter + " even numbers")
print("There are " + oddCounter + " odd numbers")


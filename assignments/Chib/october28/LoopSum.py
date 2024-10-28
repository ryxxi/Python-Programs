decision = input("Do you wish to execute this program?(Y/N): ")

while decision == "Y":

	number1 = int(input("Enter integer 1: "))
	number2 = int(input("Enter integer 2: "))
	sum = number1 + number2
	print(sum)
	
	decision = input("Do you wish to repeat this program?(Y/N): ")
bar1 = input("Enter an integer from 1-30: ")
bar1 = int(bar1)
bar2 = input("Enter an integer from 1-30: ")
bar2 = int(bar2)
bar3 = input("Enter an integer from 1-30: ")
bar3 = int(bar3)
bar4 = input("Enter an integer from 1-30: ")
bar4 = int(bar4)
bar5 = input("Enter an integer from 1-30: ")
bar5 = int(bar5)

starCounter = 0
print("\n")

if (1 < bar1 < 30) and (1 < bar2 < 30) and (1 < bar3 < 30) and (1 < bar4 < 30) and (1 < bar5 < 30):

	while (starCounter < bar1):
		print("*", end="")
		starCounter +=1

	starCounter = 0
	print("\n")

	while (starCounter < bar2):
		print("*", end="")
		starCounter +=1

	starCounter = 0
	print("\n")

	while (starCounter < bar3):
		print("*", end="")
		starCounter +=1

	starCounter = 0
	print("\n")

	while (starCounter < bar4):
		print("*", end="")
		starCounter +=1

	starCounter = 0
	print("\n")

	while (starCounter < bar5):
		print("*", end="")
		starCounter +=1

	print("\n")

else:
	print("Nuh-uh buddy, I said BETWEEN 1 and 30!\n")
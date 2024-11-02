number = float(input("Enter a number: "))

largest = number
second_largest = 0

for x in range (9):

	number = float(input("Enter a number: "))

	if number > largest:
		
		second_largest = largest
		largest = number

print(largest)
print(second_largest)
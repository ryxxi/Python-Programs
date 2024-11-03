number = float(input("Enter a number: "))

largest = number
second_largest = 0

number = float(input("Enter a number: "))

if number > largest:
	second_largest = largest
	largest = number
else:
	second_largest = number

for x in range (8):

	number = float(input("Enter a number: "))

	while number > second_largest:

		while number > largest:
			second_largest = largest
			largest = second_largest

		second_largest = largest
		largest = number

print(largest)
print(second_largest)
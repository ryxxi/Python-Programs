number = float(input("Input a number, or type -1 to end: "))
largest = number
smallest = number

while number != -1:

	number = float(input("Input a number, or type -1 to end: "))

	if number > largest:
		largest = number
	if number < smallest:
		smallest = number

print(f"Largest: {largest}\nSmallest: {smallest}")

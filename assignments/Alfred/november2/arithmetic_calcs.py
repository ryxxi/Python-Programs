number = int(input("Enter a number: "))

sum = number
product = number
smallest = number
largest = number

for x in range (3):

	number = int(input("Enter another number: "))


	sum += number
	product *= number

	if number > largest:
		largest = number
	if number < smallest:
		smallest = number


avg = sum / 4
sum = str(sum)
avg = str(avg)
product = str(product)
smallest = str(smallest)
largest = str(largest)

print("Sum is: " + sum)
print("Average is: " + avg)
print("Product is: " + product)
print("Smallest is: " + smallest)
print("Largest is: " + largest)
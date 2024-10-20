num1 = input("Enter first integer: ")
num2 = input("Enter second integer: ")
num3 = input("Enter third integer: ")

num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

sum = num1 + num2 + num3
avg = (num1 + num2 + num3) / 3
prod = num1 * num2 * num3

if ((num1 <= num2) and (num1 <= num3)):
	smallest = num1

if ((num1 >= num2) and (num1 >= num3)):
	largest = num1

if ((num2 <= num1) and (num2 <= num3)):
	smallest = num2

if ((num2 >= num1) and (num2 >= num3)):
	largest = num2

if ((num3 <= num2) and (num3 <= num1)):
	smallest = num3

if ((num3 >= num2) and (num3 >= num1)):
	largest = num3

sum = str(sum)
avg = str(avg)
prod = str(prod)
smallest = str(smallest)
largest = str(largest)

print("Sum is: " + sum)
print("Average is: " + avg)
print("Product is: " + prod)
print("Smallest is: " + smallest)
print("Largest is: " + largest)
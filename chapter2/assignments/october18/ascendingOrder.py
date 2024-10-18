num1 = input("Enter a decimal number: ")
num2 = input("Enter a decimal number: ")
num3 = input("Enter a decimal number: ")

num1 = float(num1)
num2 = float(num2)
num3 = float(num3)

if ((num1 <= num2) and (num1 <= num3)):
	smallest = num1
elif ((num1 >= num2) and (num1 >= num3)):
	largest = num1
else:
	mid = num1

if ((num2 <= num1) and (num2 <= num3)):
	smallest = num2
elif ((num2 >= num1) and (num2 >= num3)):
	largest = num2
else:
	mid = num2

if ((num3 <= num2) and (num3 <= num1)):
	smallest = num3
elif ((num3 >= num2) and (num3 >= num1)):
	largest = num3
else:
	mid = num3

smallest = str(smallest)
largest = str(largest)
mid = str(mid)

print(f"{smallest}, {mid}, {largest}")


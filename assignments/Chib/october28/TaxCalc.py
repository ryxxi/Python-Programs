name = input("Enter your name: ")
income = float(input("Enter your annual income, in $: "))

if (income < 30000):
	tax = income * 0.15

else:
	tax = income * 0.2

print(f"Total tax: {tax: ,.2f}".replace("$ ", "$"))
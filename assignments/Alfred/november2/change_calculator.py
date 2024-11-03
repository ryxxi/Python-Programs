import random
import math

price = random.uniform(1, 50)

payment_choice = (input(f"The price is ${price: .2f}. How would you like to pay: cash(1) or card(2)?: "))

if payment_choice == '1':
	payment_amount = input("How much will you be paying with?: ")
	if payment_amount.isdigit():
		payment_amount = int(payment_amount)
		if payment_amount > price:
			change = (payment_amount - price) * 100
			quarters = change // 25
			dimes_and_pennies = change % 25
			dimes = dimes_and_pennies // 10
			pennies = round(dimes_and_pennies % 10)
			print(f"""
				Thank you!

				Your change is:
				{quarters} quarters
				{dimes} dimes
				{pennies} pennies

				""")
		else:
			print("That ain't enough, you broke bum. Security!! Get this thief outta here!")
	else: 
		print("Ye, sorry we don't take whatever that is. Security!!")

elif payment_choice == '2':
	print("Thank you, have a great day!")
else:
	print("Ye, sorry we don't take whatever that is. Security!!")
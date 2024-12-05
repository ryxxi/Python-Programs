class Pizza:

	odogwu_counter = 0
	big_boys_counter = 0
	small_money_counter = 0
	sapa_counter = 0

	def get_guests(self):

		guests = input("How many guests will there be?\n")
		if guests.isdigit():
			guests = int(guests)
			if guests > 1: return guests

			else:
				print("That doesn't look right. Try again.")
				get_guests()

		else:
			print("That doesn't look right. Try again.")
			get_guests()



	def calculate_pizzas(self, guests):

		if guests >= 12:
			self.odogwu_counter += (guests//12)
			guests -= (12 * self.odogwu_counter)
			return self.calculate_pizzas(guests)

		elif guests >= 8:
			self.big_boys_counter += (guests//8)
			guests -= (8 * self.big_boys_counter)
			return self.calculate_pizzas(guests)

		elif guests >= 6:
			self.small_money_counter += (guests//6)
			guests -= (6 * self.small_money_counter)
			return self.calculate_pizzas(guests)

		elif guests >= 4:
			self.sapa_counter += (guests//4)
			guests -= (4 * self.sapa_counter)
			return self.calculate_pizzas(guests)

		elif guests >= 1:
			self.sapa_counter += 1
			guests = 0

		return guests


	def get_price(self):

		odogwu_price = 5200 * self.odogwu_counter
		big_boys_price = 4000 * self.big_boys_counter
		small_money_price = 2900 * self.small_money_counter
		sapa_price = 2500 * self.sapa_counter
	
		total = odogwu_price + big_boys_price + small_money_price + sapa_price

		return total

	def get_receipt(self, total):

		print("Your Order:\n")
		print(f"Size\tQty\tPrice\tTotal")

		if self.odogwu_counter >= 1:
			print(f"Odogwu\t{self.odogwu_counter}x\tN5200\t{5200 * self.odogwu_counter}")

		if self.big_boys_counter >= 1:
			print(f"BB\t{self.big_boys_counter}x\tN4000\t{4000 * self.big_boys_counter}")

		if self.small_money_counter >= 1:
			print(f"SM\t{self.small_money_counter}x\tN2900\t{2900 * self.small_money_counter}")

		if self.sapa_counter >= 1:
			print(f"Sapa\t{self.sapa_counter}x\tN2500\t{2500 * self.sapa_counter}")

		print(f"Your total is: NGN{total}\nThank you for your patronage!")
	






pizza = Pizza()
		
print("Welcome to Leke's Pizza Shop!")

print("""
    Choose from our wide range on pizza sizes!
____________________________________________________
    Size\tSlices\tPrice
                                                
    Sapa\t4\tN2500
    Small Money\t6\tN2900
    Big Boys\t8\tN4000
    Odogwu\t12\tN5200
____________________________________________________

""")


pizza.calculate_pizzas(pizza.get_guests())
pizza.get_receipt(pizza.get_price())


































import random
from datetime import datetime

class Checkout:

	def __init__(self, customer_name):
		self.customer_name = customer_name
		self.date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		self.item_count = 1
		self.items = []
		self.price_of_items = []
		self.quantity_of_items = []
		self.VAT = 0.175

	def get_customer_name(self):
		return self.customer_name

	def process_items(self):
		self.items.append(self.get_item())
		self.price_of_items.append(self.get_item_cost())
		self.check_for_more_items()

	def checkout(self):
		self.get_purchase_info()
		payment = float(input("How much did the customer pay? "))
		enough = self.is_enough(payment)
		self.get_receipt(enough)
		return payment

	def get_item(self):
		item = input("What did you purchase? ")
		return item

	def get_item_cost(self):
		quantity = int(input("How many units did you purchase? "))
		self.quantity_of_items.append(quantity)
		single_price = float(input("Enter the price of 1 unit: "))
		total_item_price = quantity * single_price
		return total_item_price

	def check_for_more_items(self):
		user_response = input("Do you have more items to checkout? (Y/N): ").strip().lower()

		if user_response == 'y':
			self.process_items()
		elif user_response == 'n':
			self.checkout()
		else:
			print("Invalid input")
			self.check_for_more_items()

	def get_store_info(self):
		print(
			f"SEMICOLON STORES\n"
			f"MAIN BRANCH\n"
			f"Loc: 312, HERBERT MACAULAY WAY, SABO YABA, LAGOS\n"
			f"Tel: 07458236943\n"
			f"Date: {self.date}\n"
			f"Customer: {self.get_customer_name()}"
		)

	def print_double_bars(self):
		print("=" * 50 + "\n")

	def print_single_bars(self):
		print("-" * 50 + "\n")

	def print_header(self):
		print("\tItem\tQty\tPrice\tTotal\n")

	def get_item_purchased(self, i):
		return self.items[i]

	def get_item_quantity(self, i):
		return self.quantity_of_items[i]

	def get_item_total(self, i):
		return self.price_of_items[i]

	def get_subtotal(self):
		return sum(self.price_of_items)

	def get_discount(self, subtotal):
		return int(random.uniform(0, 0.35 * subtotal))

	def get_VAT(self, subtotal):
		return subtotal * self.VAT

	def get_total(self):
		subtotal = self.get_subtotal()
		discount = self.get_discount(subtotal)
		vat = self.get_VAT(subtotal)
		total = (subtotal - discount) + vat
		return total

	def is_enough(self, payment):
		return payment >= self.get_total()

	def get_purchase_info(self):
		self.get_store_info()
		print()
		self.print_double_bars()
		self.print_header()
		self.print_single_bars()

		for i in range(len(self.items)):
			item_total = self.get_item_total(i)
			price_per_unit = item_total / self.get_item_quantity(i)
			print(f"\t{self.get_item_purchased(i)}\t{self.get_item_quantity(i)}\t{price_per_unit:.2f}\t{item_total:.2f}")
			print()

		self.print_single_bars()
		subtotal = self.get_subtotal()
		discount = self.get_discount(subtotal)
		vat = self.get_VAT(subtotal)
		total = self.get_total()

		print(f"\t\tSubtotal: {subtotal:.2f}\n")
		print(f"\t\tDiscount: {discount}\n")
		print(f"\t\tVAT: {vat:.2f}\n")
		self.print_double_bars()
		print(f"\t\tTotal: {total:.2f}\n")
		self.print_double_bars()
		print(f"\t\tKindly pay: {total:.2f}\n")
		self.print_double_bars()
		self.print_double_bars()

	def get_purchase_info_minus_payment(self):
		self.get_store_info()
		print()
		self.print_double_bars()
		self.print_header()
		self.print_single_bars()

		for i in range(len(self.items)):
			item_total = self.get_item_total(i)
			price_per_unit = item_total / self.get_item_quantity(i)
			print(f"\t{self.get_item_purchased(i)}\t{self.get_item_quantity(i)}\t{price_per_unit:.2f}\t{item_total:.2f}")
			print()

		self.print_single_bars()
		subtotal = self.get_subtotal()
		discount = self.get_discount(subtotal)
		vat = self.get_VAT(subtotal)
		total = self.get_total()

		print(f"\t\tSubtotal: {subtotal:.2f}\n")
		print(f"\t\tDiscount: {discount}\n")
		print(f"\t\tVAT: {vat:.2f}\n")
		self.print_double_bars()
		print(f"\t\tTotal: {total:.2f}\n")
		self.print_double_bars()
		self.print_double_bars()

	def get_receipt(self, is_enough):
		if is_enough:
			self.get_purchase_info_minus_payment()
			print("Thank you for your patronage")
			self.print_double_bars()
		else:
			print("Insufficient Payment")
			self.checkout()

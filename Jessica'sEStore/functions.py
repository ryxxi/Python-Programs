from menus import Menus

class Functions:

	phone_count = 0
	laptop_count = 0
	headphones_count = 0



	products = {
		"Laptop" : 1000,
		"Phone" : 500,
		"Headphones" : 100
	}

	shopping_lists = {}
	cart = {}
	shopping_lists["cart"] = cart


	def main_menu(action):

		action = input(Menus.main_menu)

		match action:

			case "0":
				action = input(Menus.main_menu)
				main_menu(0)

			case "1":
				create_delete_shopping_list(action)					

			case "2":
				view_shopping_list()

			case "3":
				action = input(Menus.add_remove_items)
				add_remove_items(action)

			case "4":
				checkout()

			case "exit":
				print("Thank you for shopping with us! Goodbye!")

			case _:
				print("Invalid input")


	def create_delete_shopping_list(action):

		action = input(Menus.create_delete_shopping_list)

		match action:

			case "1":
				create_shopping_list()

			case "2":
				delete_shopping_list()

			case "3":
				main_menu(0)

			case _:
				print("Invalid input")


	def create_shopping_list():

		list_name = input(Menus.create_shopping_list)
	
		if list_name in shopping_lists:

			print("""

				There already exists a shopping list with this name

				Try another name:

				""")

		else:

			print(f"Created a new shopping list named: {list_name}")
			shopping_lists[list_name] = {}



	def delete_shopping_list():

		list_name = input(Menus.delete_shopping_list)
	
		if list_name not in shopping_lists:

			print("""

				There doesn't exists a shopping list with this name

				Try another name:

				""")

		else:

			print(f"Deleted {list_name}")
			del shopping_lists[list_name]





	def view_shopping_list():

		shopping_list = input(Menus.checkout)

		if shopping_list in shopping_lists:

				print(f"{shopping_list}:")

				for item, quantity in shopping_lists[shopping_list].items():
					print(f"    {quantity}x {item}")

		else:
			print(f"{shopping_list} not found")



	def add_remove_items(action):

		match action:

			case "1":
				item = input(Menus.add_items)
				add_items(item)

			case "2":
				item = input(Menus.remove_items)
				remove_items(item)

			case _:
				print("Invalid input")



	
	def add_items(item):

		match item.lower():

			case "phone":
				list_name = input(Menu.add_to_where)
				number = input(Menu.how_many_add)

				if number.isdigit() and list_name in shopping_lists:
					number = int(number)
					phone_count += number
					shopping_lists[list_name]["Phone"] = phone_count

				else:
					print("Make sure you entered a number and the shopping list exists. Try again")
					add_items("phone")

			case "laptop":
				list_name = input(Menu.add_to_where)
				number = input(Menu.how_many_add)

				if number.isdigit() and list_name in shopping_lists:
					number = int(number)
					laptop_count += number
					shopping_lists[list_name]["Laptop"] = laptop_count

				else:
					print("Make sure you entered a number and the shopping list exists. Try again")
					add_items("laptop")

			case "headphones":
				list_name = input(Menu.add_to_where)
				number = input(Menu.how_many_add)

				if number.isdigit() and list_name in shopping_lists:
					number = int(number)
					headphones_count += number
					shopping_lists[list_name]["Headphones"] = headphones_count

				else:
					print("Make sure you entered a number and the shopping list exists. Try again")
					add_items("headphones")

			case _:
				("Sorry, we don't sell that item")
		



	def remove_items(item):

		match item.lower():

			case "phone":
				list_name = input(Menu.remove_from_where)
				number = input(Menu.how_many_remove)

				if number.isdigit() and list_name in shopping_lists:
					number = int(number)

					if number <= phone_count:
						phone_count -= number
						shopping_lists[list_name]["Phone"] = phone_count

					else:
						print(f"You only have {phone_count}x Phones")
						remove_items("phone")

						

				else:
					print("Make sure you entered a number and the shopping list exists. Try again")
					add_items("phone")

			case "laptop":
				list_name = input(Menu.remove_from_where)
				number = input(Menu.how_many_remove)

				if number.isdigit() and list_name in shopping_lists:
					number = int(number)
					
					if number <= phone_count:
						phone_count -= number
						shopping_lists[list_name]["Phone"] = phone_count

					else:
						print(f"You only have {phone_count}x Phones")
						remove_items("phone")

				else:
					print("Make sure you entered a number and the shopping list exists. Try again")
					add_items("laptop")

			case "headphones":
				list_name = input(Menu.remove_from_where)
				number = input(Menu.how_many_remove)

				if number.isdigit() and list_name in shopping_lists:
					number = int(number)
					
					if number <= phone_count:
						phone_count -= number
						shopping_lists[list_name]["Phone"] = phone_count

					else:
						print(f"You only have {phone_count}x Phones")
						remove_items("phone")

				elif number == "all":
					headphones_count = 0
					cart["Headphones"] = headphones_count

				else:
					print("Make sure you entered a number and the shopping list exists. Try again")
					add_items("headphones")

			case _:
				("Sorry, we don't sell that item")




		def checkout():

			shopping_list = input(Menus.checkout)

			if shopping_list in shopping_lists:

				total = 0
				print(f"""Checking out:

					'{shopping_list}':
					"""

				for item, quantity in shopping_lists[shopping_list].items():
					total += quantity
					print(f"    {quantity}x {item}")

				action = input(f"""

				Your total is {total}

				Enter 'Yes' or 'No'
						""")

				match action.lower:

					case "yes":
						print("Done! Thank you for shopping with us!")

					case _:
						print("Taking you back to the main menu...")
						main_menu(0)

			else:
				print(f"{shopping_list} not found")

			

			

			















































































		
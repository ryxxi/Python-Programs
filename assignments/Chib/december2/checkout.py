from checkout import Checkout

def main():
	name = input("Enter customer's name: ")
	checkout = Checkout(name)
	checkout.process_items()

if __name__ == "__main__":
	main()

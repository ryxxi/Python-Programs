miles = float(input("Enter miles travelled: "))
gallons = float(input("Enter gallons used: "))

miles_per_gallon = miles / gallons
total_mpg = miles_per_gallon
trips = 1

print(f"Miles per gallon from trip {trips}: {total_mpg: .2}\n")

choice = int(input("Enter 0 to continue entering values, or enter -1 to quit: "))


while choice == 0:

	miles = float(input("Enter miles travelled: "))
	gallons = float(input("Enter gallons used: "))

	milesPerGallon = miles / gallons
	total_mpg += miles_per_gallon
	trips += 1
	print(f"Miles per gallon from trip {trips}: {total_mpg: .2f}\n")
	choice = int(input("Enter 0 to continue entering values, or enter -1 to quit: "))

print(f"Total miles per gallon from {trips} trip(s): {total_mpg: .2f}\n")
number = input("Input an integer to get its digit sum: ")
sum = 0

if number.isdigit():

	for x in number:

		x = int(x)
		sum+=x

	print(f"\n{sum}\n")

else:
	print("\nNumbers don't have letters, decimal points, or anything else!\n")
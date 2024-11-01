days_late = int(input("Enter how many days late the member is: "))

if days_late >= 30:
	print("Membership is terminated")
elif days_late >= 10:
	print("5 Rupee charge")
elif days_late >= 6:
	print("1 Rupee charge")
elif days_late > 0:
	print("50 Paise charge")
else:
	print("Thank you for returning our book promptly!")
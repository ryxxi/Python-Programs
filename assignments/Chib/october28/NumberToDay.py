day = int(input("Enter an integer between 1 and 7: "))

def switch (day):

	if day == 1:
		return "Monday"

	elif day == 2:
		return "Tuesday"

	elif day == 3:
		return "Wednesday"

	elif day == 4:
		return "Thursday"

	elif day == 5:
		return "Friday"

	elif day == 6:
		return "Saturday"

	elif day == 7:
		return "Sunday"

	else:
		return "Error"

print (switch(day))
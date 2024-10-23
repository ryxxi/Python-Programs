largest = 0
a = 10
counter = 0


while counter < a:
		
	score = int(input("Enter score: "))

	if score <= 100 and score >= 1:
		counter +=1
		
		if (score > largest):
			largest = score

	else:
		print("Score is greater than 100 or less than 0")


print(f"Largest score is {largest}")
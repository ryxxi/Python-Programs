number = 1
original = number
sum = 0

for x in range (1, 13):
	for y in range (1, 21):
		print(f"{number:7}", end="")
		number += original
	original +=1
	number = 0
	number += original
	print()

		
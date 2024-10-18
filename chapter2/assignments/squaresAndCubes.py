print("Number\tSquare\tCube")

numberCounter = 0
number = 0
square = number ** 2
cube = number ** 3

while numberCounter <= 5:
	number = str(number)
	square = str(square)
	cube = str(cube)
	
	print(number + '\t' + square + '\t' + cube)

	number = int(number)
	square = int(square)
	cube = int(cube)
	
	number = number + 1
	square = number ** 2
	cube = number ** 3

	numberCounter = numberCounter + 1
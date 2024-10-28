leftSide = 1
rightSide = 1
product = leftSide * rightSide

while leftSide < 10:

	while rightSide < 10:
		product = leftSide * rightSide
		print(f"{leftSide} * {rightSide} = {product}", end="	")
		rightSide +=1


	leftSide +=1
	rightSide = 1
	print("")
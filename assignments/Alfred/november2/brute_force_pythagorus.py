pythagorean_triple_counter = 0
combinations = 0

for side_1 in range (1, 21):
	for side_2 in range (1, 21):
		for hypotenuse in range (1, 21):
			combinations +=1
			if hypotenuse == ((side_1 ** 2) + (side_2 ** 2)) ** 0.5:
				pythagorean_triple_counter += 1
				print(f"A triangle with a hypotenuse of length {hypotenuse}, adjacent of length {side_1}, and opposite of length {side_2} is a Pythagorean Triple")

		if hypotenuse == ((side_1 ** 2) + (side_2 ** 2)) ** 0.5:
			pythagorean_triple_counter += 1
			print(f"A triangle with a hypotenuse of length {hypotenuse}, adjacent of length {side_1}, and opposite of length {side_2} is a Pythagorean Triple")

	if hypotenuse == ((side_1 ** 2) + (side_2 ** 2)) ** 0.5:
		pythagorean_triple_counter += 1
		print(f"A triangle with a hypotenuse of length {hypotenuse}, adjacent of length {side_1}, and opposite of length {side_2} is a Pythagorean Triple")

print(f"When looking through values from 1-20 for all sides of a right-angles triangle, there are {pythagorean_triple_counter} Pythagorean Triples out of {combinations} combinations")
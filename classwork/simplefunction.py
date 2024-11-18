from random import randrange

def give_questions():
	right_counter = 0
	wrong_counter = 0
	count = 1
	correct_answer = [0,0,0,0,0,0,0,0,0,0]

	while count < 6:

		random1 = randrange(1,1001)
		random2 = randrange(1,1001)

		print(random1, '+', random2)

		answer = int(input("Give the answer to the above equation: "))

		if answer == random1 + random2:
			right_counter += 1

		else:
			wrong_counter += 1

		correct_answer[count - 1] = random1 + random2

		count += 1

	count = 6
	while count < 9:

		random1 = randrange(1,1001)
		random2 = randrange(1,1001)

		print(random1, 'x', random2)

		answer = int(input("Give the answer to the above equation: "))

		if answer == random1 * random2:
			right_counter += 1

		else:
			wrong_counter += 1

		correct_answer[count - 1] = random1 * random2

		count += 1

	count = 9
	while count < 11:

		random1 = randrange(1,1001)
		random2 = randrange(1,1001)

		print(random1, '-', random2)

		answer = int(input("Give the answer to the above equation: "))

		if answer == random1 - random2:
			right_counter += 1

		else:
			wrong_counter += 1

		correct_answer[count - 1] = random1 - random2

		count += 1

	print(f"\nYou got {right_counter} correct and {wrong_counter} incorrect\n")

	for value in range (0, 10):

		print(f"The correct answer for question {value + 1} is {correct_answer[value]}")		


give_questions()
import random

random = random.randint(0,1000)

guess = int(input("Guess the random number between 0 and 1000: "))

while (guess != random):

	if (guess > random):
		guess = int(input("Nuh uh, too high! Try again: "))

	if (guess < random):
		guess = int(input("Nuh uh, too low! Try again: "))

print("Well done! You guessed correct!")
from random import Random

rand = Random()
number1 = rand.randint(0, 99)
number2 = rand.randint(0, 99)

user_answer = input(f"What is the sum of {number1} and {number2}?\n")
if user_answer.isdigit():
    user_answer = int(user_answer)
    print(user_answer == number1 + number2)
else:
    print("False")

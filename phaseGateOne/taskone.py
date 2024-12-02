from random import Random

rand = Random()
integer1 = rand.randint(0, 99)
integer2 = rand.randint(0, 99)

user_answer = input(f"What is the sum of {number1} and {number2}?\n")
if user_answer.isdigit():
    user_answer = int(user_answer)
    print(user_answer == integer1 + integer2)
else:
    print("False")

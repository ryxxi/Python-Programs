from random import Random
import time

rand = Random()
correct_answers = 0
time_taken = 0
start_time = time.time()

for count in range(10):

    minuend = rand.randint(0,200)
    subtrahend = rand.randint(0,200)

    while subtrahend > minuend:
        subtrahend = rand.randint(0,200)

    user_answer = input(f"What is {minuend} - {subtrahend}\n")
    if user_answer.isdigit():
        user_answer = int(user_answer)
        if user_answer == minuend - subtrahend:
            correct_answers += 1

end_time = time.time()
time_elapsed = end_time - start_time
print(f"Your score: {correct_answers}/10")
print(f"Time taken: {time_elapsed:.0f}")
        


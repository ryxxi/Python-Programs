from random import Random
import time

rand = Random()
correct_answers = 0
time_taken = 0
start_time = 0
end_time = 0

for count in range(10):

    minuend = rand.randint(0,200)
    subtrahend = rand.randint(0,200)

    while subtrahend > minuend:
        subtrahend = rand.randint(0,200)

    start_time = time.asctime()
    user_answer = input(f"What is {minuend} - {subtrahend}\n")
    if user_answer.isdigit():
        user_answer = int(user_answer)
        if user_answer == minuend - subtrahend:
            correct_answers += 1

end_time = time.localtime()
print(f"Your score: {correct_answers}/10")
print(f"Start time: {start_time}\nEnd time: {end_time}")
        


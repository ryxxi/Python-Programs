
current_day = ""
future_day = ""

def get_current_day(day):

    match day:
    
        case 0: current_day = "Sunday"
        case 1: current_day = "Monday"
        case 2: current_day = "Tuesday"
        case 3: current_day = "Wednesday"
        case 4: current_day = "Thursday"
        case 5: current_day = "Friday"
        case 6: current_day = "Saturday"
        case _: print("Invalid input")

    return current_day

def get_future_day(day):

    if day > 6: day %= 7

    match day:
    
        case 0: future_day = "Sunday"
        case 1: future_day = "Monday"
        case 2: future_day = "Tuesday"
        case 3: future_day = "Wednesday"
        case 4: future_day = "Thursday"
        case 5: future_day = "Friday"
        case 6: future_day = "Saturday"

    return future_day


day = input("Enter today's day, with 0 being Sunday:\n")
if day.isdigit():
    day = int(day)
else:
    print("Invalid input")

elapsed = input("Enter number of days elapsed since today:\n")
if elapsed.isdigit():
    elapsed = int(elapsed)
else:
    print("Invalid input")

get_current_day(day)
print(f"Today is {get_current_day(day)}")

day += elapsed

get_future_day(day)
print(f"Future day is {get_future_day(day)}")

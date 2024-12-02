total = 0
integer = input("Enter an integer between 0 and 1000: ")
if integer.isdigit:
    for digit in integer:
        total += int(digit)
else:
    print("Invalid input")

print(total)
    

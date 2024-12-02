integers = []
count = 0

while count < 3:
    integer = input("Enter an integer: ")
    if integer.isdigit():
        integers.append(int(integer))
        count += 1
    else:
        print("Invalid input")

print(*sorted(integers), sep=", ")

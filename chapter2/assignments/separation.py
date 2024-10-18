number = input("Enter a 5 digit integer: ")
number = int(number)

digit1 = number // 10000
digit2 = (number // 1000) % 10
digit3 = (number // 100) % 10
digit4 = (number // 10) % 10
digit5 = number % 10

digit1 = str(digit1)
digit2 = str(digit2)
digit3 = str(digit3)
digit4 = str(digit4)
digit5 = str(digit5)

print(digit1 + "\t" + digit2 + "\t" + digit3 + "\t" + digit4 + "\t" + digit5)
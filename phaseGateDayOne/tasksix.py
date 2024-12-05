from random import Random

rand = Random()
characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz12345678901234567890!@£$%^&*()_+-={}[]:|<>?/.,~`"

uppers = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowers = "abcdefghijklmnopqrstuvwxyz"
numbers = "1234567890"
symbols = "!@£$%^&*()_+-={}[]:|<>?/.,~`"
secure = True

secure_password = ""

while(secure):
    
    secure_password = ""

    for count in range(16):
        secure_password += rand.choice(characters)

    if all(char not in uppers for char in secure_password):
        secure = False
        continue
    if all(char not in lowers for char in secure_password):
        secure = False
        continue
    if all(char not in numbers for char in secure_password):
        secure = False
        continue
    if all(char not in symbols for char in secure_password):
        secure = False
        continue
    break

print(secure_password)

    

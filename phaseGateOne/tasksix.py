from random import Random

rand = Random()
characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@£$%^&*()_+-={}[]:|<>?/.,~`"

secure_password = ""

for count in range(16):
    secure_password += rand.choice(characters)

print(secure_password)

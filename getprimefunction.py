def is_prime(integer):

    if integer == 2 or integer == 3: return False

    if integer <= 1 or integer % 2 == 0 or integer % 3 == 0: return False

    for i in range(, integer, 6):
        if integer % i == 0 or integer % (i + 2) == 0: return False

    return True

print(is_prime(15))
print(is_prime(11))

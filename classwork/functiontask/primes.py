numbers = [32, 76, 43, 99, 5, 88, 2345]

print(list(map(lambda x: x ** 2, filter(lambda x: x % 2 != 0, numbers))))
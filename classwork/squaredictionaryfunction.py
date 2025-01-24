def square_to_dictionary(number):
    if isinstance(number, (int, float)) and not isinstance(number, bool):
        square_dictionary = {
            1: number,
            2: number ** 2
        }
        return square_dictionary
    raise TypeError

print(square_to_dictionary(3))
        
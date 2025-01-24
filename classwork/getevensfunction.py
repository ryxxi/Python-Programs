def get_evens(anything):
    if isinstance(anything, str):
        even_counter = 0
        for char in anything:
            temp = 0
            try:
                temp = int(char)
            except ValueError:
                continue
            if temp % 2 == 0: even_counter += 1
        return even_counter
    raise TypeError
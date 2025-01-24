def encrypt(string, encryption_key):
    
    encrypted_string = ''
    if isinstance(string, str):
        for char in string:
            if char.isalpha():
                counter = 0
                while counter < encryption_key:
                    if ord(char) == 122: char = 'a'
                    elif ord(char) == 90: char = 'A'
                    else: char = chr(ord(char) + 1)
                    counter += 1
            encrypted_string += char
        return encrypted_string
    raise TypeError
    
print(encrypt("abcdefghijkl7&&mnopqrstuvwxyz", 1))
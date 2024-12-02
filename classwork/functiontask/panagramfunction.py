def check_if_panagram(string):

	alphabet = "abcdefghijklmnopqrstuvwxyz"

	return all(char in alphabet for char in string)

string1 = "hello i'm leke"
string2 = "abcdefghijklmnopqrstuvwxyz"

print(check_if_panagram(string1))
print(check_if_panagram(string2))




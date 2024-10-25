import math

sides = int(input("Input the number of sides: "))
side_length = float(input("Input the length of one side: "))

numerator = sides * (side_length ** 2)
denominator = 4 * (math.tan(3.141592 / sides))
area = numerator / denominator

print(f"The area is {area: .2f}")
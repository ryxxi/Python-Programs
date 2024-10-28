a = float(input("Enter variable a: "))
b = float(input("Enter variable b: "))
c = float(input("Enter variable c: "))

discriminant = (b ** 2) - (4 * a * c)

if (discriminant > 0):

	root1 = (-b +(discriminant ** 0.5)) / (2 * a)
	root2 = (-b -(discriminant ** 0.5)) / (2 * a)
	print(f"Root 1: {root1:.3f}\nRoot 2: {root2:.3f}")

elif (discriminant == 0):

	root = -b / (2 * a)
	print(f"Root: {root:.3f}")

else:

	real = -b / (2 * a)
	imaginary = (abs(discriminant) ** 0.5) / (2 * a)
	print(f"Root 1: {real:.3f} + {imaginary:.3f}j")
	print(f"Root 2: {real:.3f} - {imaginary:.3f}j")
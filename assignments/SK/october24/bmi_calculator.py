height = float(input("Enter your height, in m: "))

weight = float(input("Enter your weight, in kg: "))

bmi = weight / (height ** 2)

print(f"\nYour BMI is {bmi}")

if bmi >= 30:
	print("You're obese\n")

elif bmi >= 25:
	print("You're overweight\n")

elif bmi >= 18.5:
	print("You're normal weight\n")

else:
	print("You're underweight\n")
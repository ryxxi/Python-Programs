height_inch = float(input("Enter height in inches: "))
weight_lbs = float(input("Enter weight in pounds: "))

height_mtr = height_inch * 0.0254
weight_kg = weight_lbs * 0.45359237

bmi = weight_kg / (height_mtr ** 2)

print(f"Your BMI is {bmi: .2f}")
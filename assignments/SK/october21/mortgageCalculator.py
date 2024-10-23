principal = float(input("Enter how much is being borrowed, in dollars: "))

annualratepercentage = float(input("Enter the annual interest rate, in %: "))

yearduration = float(input("Enter the duration of the mortgage, in years: "))

monthlyrate = (annualratepercentage / 100) / 12
monthduration = yearduration * 12

numerator = principal * monthlyrate * ((1 + monthlyrate) ** monthduration)
denominator = ((1 + monthlyrate) ** monthduration) - 1

monthlypayment = numerator / denominator

print(f"\nThe monthly payment is ${monthlypayment:,.2f}\n".replace("$ ", "$"))
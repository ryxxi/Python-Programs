principal = input("Enter how much is being borrowed, in dollars: ")
principal = float(principal)

annualratepercentage = input("Enter the annual interest rate, in %: ")
annualratepercentage = float(annualratepercentage)

yearduration = input("Enter the duration of the mortgage, in years: ")
yearduration = float(yearduration)

monthlyrate = (annualratepercentage / 100) / 12
monthduration = yearduration * 12

numerator = principal * monthlyrate * ((1 + monthlyrate) ** monthduration)
denominator = ((1 + monthlyrate) ** monthduration) - 1

monthlypayment = numerator / denominator
roundpayment = round(monthlypayment, 2)

print(f"\nThe monthly payment is ${roundpayment}\n")






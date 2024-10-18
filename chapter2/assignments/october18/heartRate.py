age = input("Please enter your age: ")
age = int(age)

maxrate = 220 - age

uppertargetrate = (85 / 100) * maxrate
lowertargetrate = (50 / 100) * maxrate

maxrate = str(maxrate)
uppertargetrate = str(uppertargetrate)
lowertargetrate = str(lowertargetrate)

print(f"Your max heart rate is: {maxrate}")
print(f"Your target hear rate is between {lowertargetrate} and {uppertargetrate}")
lower = int(input("Input the lower bound: "))
upper = int(input("Input the upper bound: "))
divisible_by = int(input("Input what the numbers should be divisible by: "))

lower_2 = lower
checker = 0
multiple = 0

while (lower_2 < (upper - 1)):
	lower_2 +=1
	multiple = (lower_2) % divisible_by
	if (multiple == 0):
		checker +=1
	

print(f"There are {checker} number(s) between {lower} and {upper} divisible by {divisible_by}")
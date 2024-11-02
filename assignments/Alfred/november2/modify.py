number_of_students = int(input("How many students sat the test?: "))

passes = 0
failures = 0

for students in range(number_of_students):

	result = int(input("Enter result (1=pass, 2=fail): "))

	if result == 1:
		passes+=1
	else:
		failures+=1

print("Passed:", passes)
print("Failed:", failures)

if passes > 8:
	print("Bonus to instructor")
score = int(input("Enter student score: "))
passes = 0
fails = 0
students = 1

if score >= 45:
	passes +=1

else:
	fails +=1

while students < 15:
	
	score = int(input("Enter student score: "))


	if score >= 45:
		passes +=1
	
	else:
		fails +=1

	students+=1

print(f"{passes} students passed")
print(f"{fails} students failed")
import studentgradefunction

course_name = input("Input course name: ")

students = ""
while not students.isdigit():
    students = input("How many students sat these exams?: ")
students = int(students)

exams = ""
while not exams.isdigit():
    exams = input("How many exams were sat?: ")
exams = int(exams)

run = studentgradefunction.StudentGradeBook(course_name, students, exams)

run.grade_book()

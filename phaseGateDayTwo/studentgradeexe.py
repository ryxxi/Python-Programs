import studentgradefunction

course_name = input("Input course name:\n")

students = ""
while not students.isdigit():
    students = input("How many students sat these exams?:\n")
students = int(students)

exams = ""
while not exams.isdigit():
    exams = input("How many exams were sat?:\n")
exams = int(exams)

run = studentgradefunction.StudentGradeBook(course_name, students, exams)

run.grade_book()

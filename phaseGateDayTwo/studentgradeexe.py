course_name = input("Input course name", end"\n")

students = ""
while not students.isdigit():
    students = input("How many students sat these exams?", end="\n")
students = int(students)

exams = ""
while not exams.isdigit():
    exams = input("How many exams were sat?", end="\n")
exams = int(exams)

run = StudentGradeBook(course_name, students, exams)

run.grade_book

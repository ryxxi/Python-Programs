class StudentGradeBook:
    
    course_name = ""
    grades = []
    students = 0
    exams = 0
    
    def __init__(self, course_name, students, exams):
        
        self.course_name = course_name
        self.students = students
        self.exams = exams
        for _ in range(exams):
            self.grades.append([])

    def get_course_name():

        return self.course_name

    def is_grade_invalid(grade):

        if grade.isdigit():
            temp = int (grade)
            if temp <= 100 and temp >= 0: return True

        return False

    def is_exam_invalid(exam):

        if exam.isdigit():
            temp = int (exam)
            if temp >= 0 and temp <= exams: return True

        return False

    def obtain_grades():

        for student in range(students):

            for exam in range(exams):

                grade = "0"

                while is_grade_invalid(grade):

                    grade = input(f"Enter Student {student+1}'s grade in Exam {exam+1}", end="\n")
                    if not is_grade_invalid(grade):
                        print("Invalid input, try again")
                        
                grades[student][exam].append(int (grade))

        return None

    def print_specific_single_bars():

        for _ in range(50):
            print("-", end="")

        print()


    def print_specific_double_bars():

        for _ in range(50):
            print("+", end="")

        print()


    def print_all_single_bars():

        for _ in range(80):
            print("-", end="")

        print()


    def print_all_double_bars():

        for _ in range(80):
            print("=", end="")

        print()


    def get_exam_total(exam):

        total = 0

        for student in range(students):
            total += grades[student][exam-1]
            
        return total


    def get_exam_mean(exam):

        mean = get_exam_total(exam) / students

        return mean
    

    def get_highest_scorer(exam):

        highest_grade = grades[0][exam-1]
        best_student = 1

        for student in range(students):

            if grades[student][exam-1] > highest_grade:

                highest_grade = grades[student][exam-1]
                best_student = student+1

        print(f"Exam {exam}'s highest grade is {highest_grade}, achieved by Student {best_student}")


    def print_specific_bar_chart(exam):

        print(f"Exam {exam}'s Distribution of Results:")
        print_specific_single_bars()

        frequency = [0,0,0,0,0,0,0,0,0,0,0]

        for student in range(students):

            percentage = grades[student][exam] // 10
            frequency[percentage] += 1

        for count in range(11):

            if count == 10: print(f"{100:>5}")

            else: print(f"{count*10:0>2}-{(count*10)+9:0>2}")

            for stars in range(frequency[count]):

                print("*", end=" ")

    def display_specific_exam():

        user_input = "0"

        while is_exam_invalid(exam):
            user_input = input(f"Which exam's grades do you wish to view? (1 - {exams})")
            if not is_exam_invalid(exam):
                print("Invalid input, try again")

        exam = int (user_input)

        print("\033[H\033[2J")

        print(f"{get_course_name()}\nExam {exam}")

        print_specific_single_bars()

        for student in range(students):
            print(f"Student {student+1}: {grades[student][exam]}\n")

        print_specific_single_bars()
        print_specific_single_bars()

        print(f"TOTAL Grade: {get_exam_total(exam)}")
        print(f"TOTAL Grade: {get_exam_mean(exam):.1f}")

        get_highest_scorer(exam)

        print_specific_double_bars()
        print_specific_double_bars()

        print_specific_bar_chart()


    def get_student_total(student):

        total = 0

        for exam in range(exams):

            total += grades[student][exam]

        return total

    def get_student_mean(student):

        mean = get_student_total(student) / exams

        return mean

    def get_all_total():

        total = 0

        for student in range(students):

            for exam in range(exams):

                total += grades[student][exam]

        return total

    def get_all_mean():

        mean = get_all_total / (students * exams)

        return mean

    def print_all_bar_chart():

        print(f"Overall Distribution of Results:")
        print_specific_single_bars()

        frequency = [0,0,0,0,0,0,0,0,0,0,0]

        for student in range(students):

            for exam in range(exams):

                percentage = grades[student][exam] // 10
                frequency[percentage] += 1

        for count in range(11):

            if count == 10: print(f"{100:>5}")

            else: print(f"{count*10:0>2}-{(count*10)+9:0>2}")

            for stars in range(frequency[count]):

                print("*", end=" ")

    def display_all_students():

        for student in range(students):

            print(f"Stud{student+1}", end="")

            for exam in range(exams):

                print(f"\t{grades[student][exam]}")

        print("\t{get_student_total(student)}", end="")
        print("\t{get_student_mean(student)}", end="")
        print("\n")

    
    def display_all_exams():

        print("Student", end="")

        for exam in range(exams):

            print("\tExam{exam+1}", end="")

        print("\tMean\tTotal")

        display_all_students()
        print_all_single_bars()
        print(f"TOTAL: {get_all_total()}")
        print(f"MEAN: {get_all_mean()}")

        print_all_single_bars()
        print_all_single_bars()

        print_all_bar_chart()
              

    def output_grades():

        print("\033[H\033[2J")

        user_choice = input("""
    Select:

    1. View Specific Exam Results
    2. View All Exam Results

    """)

        match user_choice:

            case "1":
                display_specific_exam()

            case "2":
                display_all_exams()

            case _:
                print("Invalid input, try again")
                display_all()


    def display_all():

        user_choice = ""

        while user_choice.upper() != "Y":

            output_grades()

            user_choice = input("Enter 'Y' to continue viewing, or enter any other key to exit")

        
    def grade_book():

        grades = obtain_grades()
        display_all()

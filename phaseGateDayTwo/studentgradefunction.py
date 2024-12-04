import time

class StudentGradeBook:
    
    course_name = ""
    grades = []
    students = 0
    exams = 0
    
    def __init__(self, course_name, students, exams):
        
        self.course_name = course_name
        self.students = students
        self.exams = exams
        self.grades = [[0] * exams for _ in range(students)]

    def get_course_name(self):

        return self.course_name

    def is_grade_valid(self, grade):

        if grade.isdigit():
            temp = int (grade)
            if temp <= 100 and temp >= 0: return True

        return False

    def is_exam_valid(self, exam):

        if exam.isdigit():
            temp = int (exam)
            if temp >= 1 and temp <= self.exams: return True

        return False

    def obtain_grades(self):

        for student in range(self.students):

            for exam in range(self.exams):

                while True:

                    time.sleep(0.5)
                    print("\033[H\033[2J")

                    grade = input(f"Enter Student {student+1}'s grade in Exam {exam+1}\n")
                    if self.is_grade_valid(grade):
                        break
                    print("Invalid input, try again")
                        
                self.grades[student][exam] = int (grade)

        return None

    def print_specific_single_bars(self):

        for _ in range(50):
            print("-", end="")

        print()


    def print_specific_double_bars(self):

        for _ in range(50):
            print("=", end="")

        print()


    def print_all_single_bars(self):

        for _ in range(60):
            print("-", end="")

        print()


    def print_all_double_bars(self):

        for _ in range(60):
            print("=", end="")

        print()


    def get_exam_total(self, exam):

        total = 0

        for student in range(self.students):
            total += self.grades[student][exam-1]
            
        return total


    def get_exam_mean(self, exam):

        mean = self.get_exam_total(exam) / self.students

        return mean
    

    def get_highest_scorer(self, exam):

        highest_grade = self.grades[0][exam-1]
        best_student = 1

        for student in range(self.students):

            if self.grades[student][exam-1] > highest_grade:

                highest_grade = self.grades[student][exam-1]
                best_student = student+1

        print(f"Exam {exam}'s highest grade is {highest_grade}, achieved by Student {best_student}")

        return highest_grade

    def print_specific_bar_chart(self, exam):

        print(f"Exam {exam}'s Distribution of Results:")
        self.print_specific_single_bars()

        frequency = [0,0,0,0,0,0,0,0,0,0,0]

        for student in range(self.students):

            percentage = self.grades[student][exam-1] // 10
            frequency[percentage] += 1

        for count in range(11):

            if count == 10: print(f"{100:>5}:", end=" ")

            else: print(f"{count*10:0>2}-{(count*10)+9:0>2}:", end=" ")

            for stars in range(frequency[count]):

                print("* ", end="")

            print()

    def get_exam_position(self, student, exam):

        student_score = self.grades[student][exam-1]
        position = 1

        for i in range(self.students):

            if i != student and self.grades[i][exam-1] > student_score:

                position += 1

        return position

    def get_overall_position(self, student):

        student_mean = self.get_student_mean(student)
        position = 1

        for i in range(self.students):

            if i != student and self.get_student_mean(i) > student_mean:

                position += 1

        return position

    def display_specific_exam(self):
        
        while True:
            user_input = input(f"Which exam's grades do you wish to view? (1 - {self.exams})\n")
            if self.is_exam_valid(user_input):
                break
            print("Invalid input, try again")

        exam = int (user_input)

        print("\033[H\033[2J")

        print(f"{self.get_course_name()}\nExam {exam}")

        self.print_specific_single_bars()

        for student in range(self.students):
            print(f"Student {student+1}: {self.grades[student][exam-1]}  ({self.get_exam_position(student, exam)})")

        self.print_specific_single_bars()
        self.print_specific_single_bars()

        print(f"TOTAL Grade: {self.get_exam_total(exam)}")
        print(f"TOTAL Grade: {self.get_exam_mean(exam):.1f}")

        self.get_highest_scorer(exam)

        self.print_specific_double_bars()
        self.print_specific_double_bars()

        self.print_specific_bar_chart(exam)


    def get_student_total(self, student):

        total = 0

        for exam in range(self.exams):

            total += self.grades[student][exam]

        return total

    def get_student_mean(self, student):

        mean = self.get_student_total(student) / self.exams

        return mean

    def get_all_total(self):

        total = 0

        for student in range(self.students):

            for exam in range(self.exams):

                total += self.grades[student][exam]

        return total

    def get_all_mean(self):

        mean = self.get_all_total() / (self.students * self.exams)

        return mean

    def print_all_bar_chart(self):

        print(f"Overall Distribution of Results:")
        self.print_all_single_bars()

        frequency = [0,0,0,0,0,0,0,0,0,0,0]

        for student in range(self.students):

            for exam in range(self.exams):

                percentage = self.grades[student][exam] // 10
                frequency[percentage] += 1

        for count in range(11):

            if count == 10: print(f"{100:>5}:", end=" ")

            else: print(f"{count*10:0>2}-{(count*10)+9:0>2}:", end=" ")

            for stars in range(frequency[count]):

                print("*", end=" ")

            print()

        self.print_all_double_bars()

    def display_all_students(self):

        for student in range(self.students):

            print(f"Stud{student+1}", end="")

            for exam in range(self.exams):

                print(f"\t{self.grades[student][exam]}", end="")

            print(f"\t{self.get_student_total(student)}", end="")
            print(f"\t{self.get_student_mean(student):.1f}", end="")
            print(f"\t{self.get_overall_position(student)}")

    
    def display_all_exams(self):

        print("Student", end="")

        for exam in range(self.exams):

            print(f"\tExam{exam+1}", end="")

        print("\tTotal\tMean\tPos")

        self.display_all_students()
        self.print_all_single_bars()
        print(f"TOTAL: {self.get_all_total()}")
        print(f"MEAN: {self.get_all_mean():.1f}")

        self.print_all_double_bars()
        self.print_all_double_bars()

        self.print_all_bar_chart()
              

    def output_grades(self):
        
        print("\033[H\033[2J")

        user_choice = input("""
    Select:

    1. View Specific Exam Results
    2. View All Exam Results

    """)

        match user_choice:

            case "1":
                time.sleep(0.5)
                print("\033[H\033[2J")
                time.sleep(0.5)
                self.display_specific_exam()

            case "2":
                time.sleep(0.5)
                print("\033[H\033[2J")
                time.sleep(0.5)
                self.display_all_exams()

            case _:
                print("Invalid input, try again")


    def display_all(self):

        while True:

            self.output_grades()

            user_choice = input("Enter 'Y' to continue viewing, or enter any other key to exit:\n")
            if user_choice.upper() != "Y": break

        
    def grade_book(self):

        self.obtain_grades()
        self.display_all()

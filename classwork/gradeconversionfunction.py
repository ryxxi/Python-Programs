student_scores = {}

def convert_grade(name, grade):
    if isinstance(name, str) and isinstance(grade, int):
        if grade > 100 or grade < 0: raise ValueError
        elif grade >= 91: grade = "Outstanding"
        elif grade >= 81: grade = "Exceeds Expectations"
        elif grade >= 71: grade = "Acceptable"
        elif grade >= 0: grade = "Fail"
            
        student_scores[name] = grade
        return student_scores
    else: raise TypeError
        
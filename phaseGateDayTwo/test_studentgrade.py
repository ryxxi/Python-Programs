from unittest import TestCase
from studentgradefunction import *

class TestStudentGradeBook(TestCase):

    def test_initialization(self):
        tester = StudentGradeBook("Math", 3, 2)
        self.assertEqual(tester.course_name, "Math")
        self.assertEqual(tester.students, 3)
        self.assertEqual(tester.exams, 2)
        self.assertEqual(tester.grades, [[0, 0], [0, 0], [0, 0]])

    def test_grade_validation(self):
        tester = StudentGradeBook("Math", 3, 2)
        self.assertTrue(tester.is_grade_valid("85"))
        self.assertFalse(tester.is_grade_valid("-5"))
        self.assertFalse(tester.is_grade_valid("110"))
        self.assertFalse(tester.is_grade_valid("abc"))

    def test_exam_validation(self):
        tester = StudentGradeBook("Math", 3, 2)
        self.assertTrue(tester.is_exam_valid("1"))
        self.assertFalse(tester.is_exam_valid("3"))
        self.assertFalse(tester.is_exam_valid("abc"))

    def test_exam_total_and_mean(self):
        tester = StudentGradeBook("Math", 3, 2)
        tester.grades = [[90, 80], [70, 60], [50, 40]]
        self.assertEqual(tester.get_exam_total(1), 210)  
        self.assertEqual(tester.get_exam_mean(1), 70.0)  

    def test_highest_scorer(self):
        tester = StudentGradeBook("Math", 3, 2)
        tester.grades = [[90, 80], [70, 95], [50, 40]]
        self.assertEqual(tester.get_highest_scorer(2),(95))

    def test_bar_chart_distribution(self):
        tester = StudentGradeBook("Math", 3, 2)
        tester.grades = [[95, 85], [75, 65], [45, 35]]


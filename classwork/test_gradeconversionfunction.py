from unittest import TestCase
from gradeconversionfunction import convert_grade

class TestGradeConversionFunction(TestCase):
    
    def test_function_exists(self):
        convert_grade("Gloria", 88)
        convert_grade("Divine", 78)
        convert_grade("Esther", 65)
        convert_grade("Mercy", 75)
        
    def test_function_returns_correctly(self):
        actual = convert_grade("Uzo", 71)
        expected = {'Gloria': 'Exceeds Expectations', 'Divine': 'Acceptable', 'Esther': 'Fail', 'Mercy': 'Acceptable', 'Uzo': 'Acceptable'}
        self.assertEqual(actual, expected)
        
    def test_function_handles_invalid_arguments(self):
        self.assertRaises(TypeError, convert_grade, "Leke", "Well done")
        self.assertRaises(TypeError, convert_grade, False, 58)
        self.assertRaises(ValueError, convert_grade, "Leke", 105)
        self.assertRaises(ValueError, convert_grade, "Leke", -9)
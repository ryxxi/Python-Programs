from unittest import TestCase
from squaredictionaryfunction import square_to_dictionary

class TestSquareDictionaryFunction(TestCase):
    
    def test_function_exists(self):
        square_to_dictionary(30)
        
    def test_function_returns_correctly(self):
        actual = square_to_dictionary(4)
        expected = {1: 4, 2: 16}
        self.assertEqual(actual, expected)
        
    def test_function_handles_invalid_arguments(self):
        self.assertRaises(TypeError, square_to_dictionary, "hello")
        self.assertRaises(TypeError, square_to_dictionary, True)
        self.assertRaises(TypeError, square_to_dictionary, None)
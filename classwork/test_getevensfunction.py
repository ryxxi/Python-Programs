from unittest import TestCase
from getevensfunction import get_evens

class TestGetEvensFunction(TestCase):
    
    def test_function_exists(self):
        get_evens("3245yhrtgewegt4h5ju")
        
    def test_function_returns_correctly(self):
        actual = get_evens("12345fhsanfj6789")
        expected = 4
        self.assertEqual(actual, expected)
        
    def test_function_with_invalid_arguments(self):
        self.assertRaises(TypeError, get_evens, 12)
        self.assertRaises(TypeError, get_evens, True)
        self.assertRaises(TypeError, get_evens, 9.43)
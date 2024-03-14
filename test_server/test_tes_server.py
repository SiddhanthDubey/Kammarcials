import unittest
from app import Welcome, Home_page

class TestAppFunctions(unittest.TestCase):
    def test_welcome_function(self):
        expected_output = "Hello World"
        result = Welcome()
        self.assertEqual(result, expected_output)

    def test_home_page_function(self):
        expected_output = "This is the home page"
        result = Home_page()
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()

import unittest
import requests


class TestWelcomeEndpoint(unittest.TestCase):
    def test_welcome_endpoint(self):
        response = requests.get('http://127.0.0.1:5000/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello World', response.content)


class TestHomePageEndpoint(unittest.TestCase):
    def test_home_page_endpoint(self):
        response = requests.get('http://127.0.0.1:5000/home')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'This is the home page', response.content)


if __name__ == '__main__':
    unittest.main()

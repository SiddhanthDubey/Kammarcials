import unittest
import requests


class TestLoginEndpoints(unittest.TestCase):
    def setUp(self):
        # Set up the base URL for your API
        self.base_url = "http://localhost:5000"  # Change this to your API URL
        # You may need to adjust the URL based on your development environment

    def test_invalid_password(self):
        # Test invalid password
        login_data = {'email': 'ss@ss.ss', 'password': 'aa'}
        response = requests.post(f"{self.base_url}/login", data=login_data)
        self.assertEqual(response.status_code, 201)
        self.assertIn('message', response.json())
        self.assertEqual(response.json()['message'], 'Invalid Password')

    def test_invalid_email(self):
        # Test invalid email
        login_data = {'email': 'iad@dsf.add', 'password': 'asdada'}
        response = requests.post(f"{self.base_url}/login", data=login_data)
        self.assertEqual(response.status_code, 201)
        self.assertIn('message', response.json())
        self.assertEqual(response.json()['message'], 'Invalid email')

    def test_google_login(self):
        # Test Google login endpoint
        google_login_data = {'email': 'test@example.com'}  # Assuming this email exists in your database
        response = requests.post(f"{self.base_url}/validate", data=google_login_data)
        self.assertIn(response.status_code, [200, 201])  # Either user found or not found

    def test_logout(self):
        # Test logout endpoint
        response = requests.get(f"{self.base_url}/logout")
        self.assertEqual(response.status_code, 200)

    def test_valid_login(self):
        # Test valid login
        login_data = {'email': 'ss@ss.ss', 'password': 'ss'}
        response = requests.post(f"{self.base_url}/login", data=login_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('user_id', response.json())
        self.assertIn('email', response.json())

'''
    def test_missing_fields(self):
        # Test missing fields
        login_data = {'email': 'validuser@example.com'}  # No password field
        response = requests.post(f"{self.base_url}/login", data=login_data)
        self.assertEqual(response.status_code, 500)
        self.assertIn('message', response.json())


    def test_server_error(self):
        # Test server error
        login_data = {'email': 'validuser@example.com', 'password': 'validpassword'}
        response = requests.post(f"{self.base_url}/login", data=login_data)
        # Assuming the server is down, it returns a 500 status code
        self.assertEqual(response.status_code, 500)
        self.assertIn('message', response.json())
        self.assertEqual(response.json()['message'], 'An error occurred while processing your request to Login')
'''

if __name__ == "__main__":
    unittest.main()

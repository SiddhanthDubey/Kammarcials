import unittest
import requests


class TestRegisterEndpoints(unittest.TestCase):
    def setUp(self):
        # Set up the base URL for your API
        self.base_url = "http://localhost:5000"  # Change this to your API URL
        # You may need to adjust the URL based on your development environment

    def test_google_register_success(self):
        # Test successful Google registration
        register_data = {'email': 'rand@example.com', 'mobile': '1234567890', 'age': 25}
        response = requests.post(f"{self.base_url}/google_register", data=register_data)
        self.assertEqual(response.status_code, 201)
        self.assertIn('user_id', response.json())
        self.assertIn('message', response.json())
        self.assertEqual(response.json()['message'], 'User registered successfully')

    def test_google_register_existing_email(self):
        # Test Google registration with existing email
        register_data = {'email': 'ss@ss.ss', 'mobile': '1234567890', 'age': 25}
        response = requests.post(f"{self.base_url}/google_register", data=register_data)
        self.assertEqual(response.status_code, 400)
        self.assertIn('message', response.json())
        self.assertEqual(response.json()['message'], 'Email already exists')

    def test_register_success(self):
        # Test successful registration
        register_data = {'email': 'test@example.com', 'password': 'password123', 'age': 25,
                         'first_name': 'John', 'last_name': 'Doe'}
        response = requests.post(f"{self.base_url}/register", data=register_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('user_id', response.json())
        self.assertIn('message', response.json())
        self.assertEqual(response.json()['message'], 'User registered successfully')

    def test_register_existing_email(self):
        # Test registration with existing email
        register_data = {'email': 'aaa@aaa.aaa', 'password': 'password123', 'age': 25,
                         'first_name': 'John', 'last_name': 'Doe'}
        response = requests.post(f"{self.base_url}/register", data=register_data)
        self.assertEqual(response.status_code, 400)
        self.assertIn('message', response.json())
        self.assertEqual(response.json()['message'], 'Email already exists')


'''
    def test_google_register_missing_fields(self):
        # Test Google registration with missing fields
        register_data = {'email': 'test@example.com', 'mobile': '1234567890'}  # Missing 'age'
        response = requests.post(f"{self.base_url}/google_register", data=register_data)
        self.assertEqual(response.status_code, 500)
        self.assertIn('message', response.json())
        
    def test_register_missing_fields(self):
        # Test registration with missing fields
        register_data = {'email': 'test@example.com',
                         'password': 'password123'}  # Missing 'age', 'first_name', 'last_name'
        response = requests.post(f"{self.base_url}/register", data=register_data)
        self.assertEqual(response.status_code, 500)
        self.assertIn('message', response.json())

    def test_server_error(self):
        # Test server error
        # Assuming the server is down, it returns a 500 status code
        register_data = {'email': 'test@example.com', 'password': 'password123', 'age': 25,
                         'first_name': 'John', 'last_name': 'Doe'}
        response = requests.post(f"{self.base_url}/register", data=register_data)
        self.assertEqual(response.status_code, 500)
        self.assertIn('message', response.json())
'''

if __name__ == "__main__":
    unittest.main()

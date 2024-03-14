import unittest
import requests
from flask import session

class TestQueryController(unittest.TestCase):
    def setUp(self):
        # Set up the base URL for your API
        self.base_url = "http://localhost:5000"  # Change this to your API URL
        # You may need to adjust the URL based on your development environment

    def test_user_query_success(self):
        # Test successful user query submission
        query_data = {'email': 'test@example.com', 'name': 'John Doe', 'query': 'Test query'}
        # Assuming a valid user session, replace 'user_id' with the actual user ID
        # This assumes that you're testing a user query with an active session
        ses = {'user_id': session.get('user_id')}
        response = requests.post(f"{self.base_url}/user_query", data=query_data, cookies=ses)
        self.assertEqual(response.status_code, 201)
        self.assertIn('message', response.json())
        self.assertEqual(response.json()['message'], 'User query received successfully')


'''
    def test_user_query_missing_fields(self):
        # Test user query with missing fields
        query_data = {'email': 'test@example.com', 'name': 'John Doe'}  # Missing 'query'
        response = requests.post(f"{self.base_url}/user_query", data=query_data)
        self.assertEqual(response.status_code, 500)
        self.assertIn('message', response.json())

    def test_server_error(self):
        # Test server error
        query_data = {'email': 'test@example.com', 'name': 'John Doe', 'query': 'Test query'}
        response = requests.post(f"{self.base_url}/user_query", data=query_data)
        # Assuming the server is down, it returns a 500 status code
        self.assertEqual(response.status_code, 500)
        self.assertIn('message', response.json())
'''

if __name__ == "__main__":
    unittest.main()

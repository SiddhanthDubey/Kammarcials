import unittest
import requests


class TestSurveyEndpoints(unittest.TestCase):
    def setUp(self):
        # Set up the base URL for your API
        self.base_url = "http://localhost:5000"  # Change this to your API URL
        # You may need to adjust the URL based on your development environment

    def test_get_survey_success(self):
        # Test successful retrieval of survey details
        # Assuming a valid user session, replace 'user_id' and 'age' with the actual user ID and age
        session = {'user_id': 'user_id', 'age': 25}
        response = requests.get(f"{self.base_url}/get_survey", cookies=session)
        self.assertEqual(response.status_code, 200)
        self.assertIn('result', response.json())

    def test_get_survey_question_success(self):
        # Test successful retrieval of survey questions
        # Assuming a valid survey_id, replace 'survey_id' with the actual survey ID
        survey_id = 'survey_id'
        response = requests.get(f"{self.base_url}/get_survey_question", params={'survey_id': survey_id})
        self.assertEqual(response.status_code, 200)
        self.assertIn('result', response.json())

    def test_submit_survey_success(self):
        # Test successful submission of survey response
        survey_data = {'q1': 'a', 'q2': 'a', 'q3': 'a', 'q4': 'a', 'q5': 'a', 'q6': 'a', 'q7': 'a', 'q8': 'a',
                       'q9': 'a', 'q10': 'a', 'q11': 'a', 'q12': 'a', }  # Add responses for all questions
        # Assuming a valid user session and survey ID, replace 'user_id' and 'survey_id' with the actual IDs

        response = requests.post(f"{self.base_url}/submit_survey", data=survey_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', response.json())


'''
    def test_get_survey_missing_age(self):
        # Test when user's age is missing in the session
        session = {'user_id': 'user_id'}  # Missing 'age' in session
        response = requests.get(f"{self.base_url}/get_survey", cookies=session)
        self.assertEqual(response.status_code, 404)
        self.assertIn('message', response.json())

    
    def test_submit_survey_incomplete(self):
        # Test submission of incomplete survey response
        survey_data = {'q1': 'response1', 'q2': 'response2'}  # Add responses for all questions
        # Assuming a valid user session and survey ID, replace 'user_id' and 'survey_id' with the actual IDs
        session = {'user_id': 'user_id', 'survey_id': 'survey_id'}
        survey_data['response_status'] = 'incomplete'
        response = requests.post(f"{self.base_url}/submit_survey", data=survey_data, cookies=session)
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', response.json())
'''

if __name__ == "__main__":
    unittest.main()

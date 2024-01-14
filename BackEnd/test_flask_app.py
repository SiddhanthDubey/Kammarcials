import unittest
import requests
import subprocess
import time


class TestFlaskApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Start the Flask app in a separate process
        cls.flask_process = subprocess.Popen(['python', 'app.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        cls.max_retries = 10
        cls.server_started = cls._wait_for_server_start()

    @classmethod
    def tearDownClass(cls):
        # Stop the Flask app process only if the server was successfully started
        if cls.server_started:
            cls.flask_process.terminate()

    @classmethod
    def _wait_for_server_start(cls):
        for _ in range(cls.max_retries):
            time.sleep(2)
            response = cls._make_request('http://127.0.0.1:5000/')
            if response and response.status_code == 200:
                return True
            print("Waiting for the server to start...")
        print("Failed to start the server within the specified retries.")
        return False

    @classmethod
    def _make_request(cls, url):
        try:
            response = requests.get(url)
            print(f"Attempted connection to {url}, status code: {response.status_code}")
            return response
        except requests.exceptions.ConnectionError:
            print(f"Connection attempt to {url} failed.")
            return None

    def test_welcome_route(self):
        response = self._make_request('http://127.0.0.1:5000/')
        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "Hello World")

    def test_home_route(self):
        response = self._make_request('http://127.0.0.1:5000/home')
        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "This is the home page")


if __name__ == '__main__':
    # Run the tests and keep track of whether they were successful
    test_result = unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestFlaskApp))

    # Check if the tests were successful and the server was started
    if test_result.wasSuccessful() and TestFlaskApp.server_started:
        print("All tests passed. Server will continue running.")
    else:
        # Stop the server if the tests failed or the server was not started
        TestFlaskApp.server_started = False
        TestFlaskApp.tearDownClass()
        print("Tests failed. Server stopped.")

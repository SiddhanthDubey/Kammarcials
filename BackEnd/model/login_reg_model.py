import mysql.connector
from flask import make_response
import logging


class AppLogger:
    def __init__(self, log_file='login_reg.log'):
        logging.basicConfig(filename=log_file, level=logging.INFO)
        self.logger = logging.getLogger()

    def log_info(self, message):
        self.logger.info(message)

    def log_error(self, message):
        self.logger.error(message)


# Create a logger instance for your module or script
logger_login = AppLogger()


class Login:
    def __init__(self):
        try:
            self.con = mysql.connector.connect(host="localhost", user='root', password="",
                                               database="kammarcials")
            self.con.autocommit = True
            self.cur = self.con.cursor(dictionary=True)
            logger_login.log_info("Connection Successful")
        except Exception as e:
            logger_login.log_error(f"Error during connection: {e}")

    def login_model(self, data):
        try:
            # Use parameterized query to prevent SQL injection
            self.cur.execute("SELECT id FROM users WHERE username = %s AND password = %s",
                             (data['username'], data['password']))

            # Fetch the result
            result = self.cur.fetchone()

            if result:
                # Successful login
                return make_response({"message": "Login successful", "id": result['id']}, 200)
            else:
                # Invalid credentials
                return make_response({"message": "Invalid username or password"}, 401)

        except Exception as e:
            # Log the error
            logger_login.log_error(f"Error in login_model: {e}")
            return make_response({"message": f"An error occurred while processing your request to Login: {e}"}, 500)


class Register:
    def __init__(self):
        try:
            self.con = mysql.connector.connect(host="localhost", user='root', password="",
                                               database="kammarcials")
            self.con.autocommit = True
            self.cur = self.con.cursor(dictionary=True)
            logger_login.log_info("Connection Successful")
        except Exception as e:
            logger_login.log_error(f"Error during connection: {e}")

    def register_model(self, data):
        try:
            self.cur.execute(
                f"INSERT INTO users(username, password) VALUES('{data['username']}', '{data['password']}')")
            user_id = self.cur.lastrowid  # Get the ID of the last inserted row
            logger_login.log_info(f"Added user with ID {user_id}: {data}")
            return make_response({"message": "User registered successfully", "user_id": user_id}, 201)
        except Exception as e:
            logger_login.log_error(f"Error in register_model: {e}")
            return make_response({"message": f"An error occurred while processing your request to register : {e}"}, 500)

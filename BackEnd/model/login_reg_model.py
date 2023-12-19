import mysql.connector
from flask import make_response
import logging
from controller.error_controller import AppLogger


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
            self.cur.execute(
                "SELECT id FROM users WHERE username = %s AND password = %s",
                (data['username'], data['password'])
            )
            user_id = self.cur.fetchone()  # Fetch the first result
            if user_id:
                logger_login.log_info(f"User Found: {data}")
                return make_response({"message": "Login Successful", "id": user_id['id']}, 201)
            else:
                logger_login.log_info(f"User not found: {data}")
                return make_response({"message": "Invalid username or password"}, 401)
        except Exception as e:
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

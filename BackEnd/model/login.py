import mysql.connector
from security.encryption import Encryption
from flask import make_response
from app import app

import json

encryption = Encryption(key=11)


class Login:
    def __init__(self):
        try:
            self.con = mysql.connector.connect(host="localhost", user='root', password="",
                                               database="kammarcials")
            self.con.autocommit = True
            self.cur = self.con.cursor(dictionary=True)
            app.logger.info("Connection Successful")
        except Exception as e:
            app.logger.error(f"Error during connection: {e}")

    def login_model(self, data):
        try:
            decoded_data = json.loads(data)
            encrypted_password = encryption.encrypt(decoded_data['password'])
            self.cur.execute("SELECT id FROM users WHERE username = %s AND password = %s",
                             (decoded_data['username'], encrypted_password))

            result = self.cur.fetchone()

            if result:
                app.logger.info(f"Successful login for user: {decoded_data['username']}")
                return make_response(
                    {"message": "Login successful", "id": result['id'], "username": decoded_data['username']}, 200)
            else:
                app.logger.warning(f"Invalid login attempt for user: {decoded_data['username']}")
                return make_response({"message": "Invalid username or password"}, 401)

        except Exception as e:
            app.logger.error(f"Error in login_model: {e}")
            return make_response({"message": f"An error occurred while processing your request to Login: {e}"}, 500)

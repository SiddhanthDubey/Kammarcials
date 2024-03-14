import mysql.connector
from security.encryption import Encryption
from flask import make_response
from app import *


encryption = Encryption(key=11)


class Register:
    def __init__(self):
        try:
            self.con = mysql.connector.connect(host=sql_host, user=sql_user, password=sql_password,
                                               database="kammarcials")
            self.con.autocommit = True
            self.cur = self.con.cursor(dictionary=True)
            app.logger.info("Connection Successful")
        except Exception as e:
            app.logger.error(f"Error during connection: {e}")

    def google_register_model(self, data):
        try:
            # Check if email already exists
            self.cur.execute("SELECT id FROM google_users WHERE email = %s", (data['email'],))
            existing_user = self.cur.fetchone()
            if existing_user:
                return make_response({"message": "Email already exists"}, 400)

            self.cur.execute(
                "INSERT INTO google_users(email, mobile, age) VALUES(%s, %s, %s)",
                (data['email'], data['mobile'], data['age'])
            )
            user_id = self.cur.lastrowid  # Get the ID of the last inserted row
            app.logger.info(f"Added user with ID {user_id}")
            return make_response({"message": "User registered successfully", "user_id": user_id}, 201)
        except Exception as e:
            app.logger.error(f"Error in google_register_model: {e}")
            return make_response({"message": f"An error occurred while processing your request to register: {e}"}, 500)

    def register_model(self, data):
        try:
            # Check if email already exists
            self.cur.execute("SELECT id FROM users WHERE email = %s", (data['email'],))
            existing_user = self.cur.fetchone()
            if existing_user:
                return make_response({"message": "Email already exists"}, 400)

            encrypted_password = encryption.encrypt(data['password'])
            self.cur.execute(
                "INSERT INTO users(password, email, age, first_name, last_name) VALUES(%s, %s, %s, %s, %s)",
                (encrypted_password, data['email'], data['age'], data['first_name'], data['last_name'])
            )

            user_id = self.cur.lastrowid  # Get the ID of the last inserted row
            app.logger.info(f"Added user with ID {user_id}")
            return make_response({"message": "User registered successfully", "user_id": user_id}, 200)
        except Exception as e:
            app.logger.error(f"Error in register_model: {e}")
            return make_response({"message": f"An error occurred while processing your request to register: {e}"}, 500)
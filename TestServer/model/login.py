import json
# import threading

import mysql.connector
from flask import make_response, session  # , jsonify
# from threading import Thread
from security.encryption import Encryption
# from controller.coupon_controller import coupon
from app import app

encryption = Encryption(key=11)


class Login:
    def __init__(self):
        # self.coupon_thread = None
        try:
            self.con = mysql.connector.connect(host="localhost", user='root', password="1234567890",
                                               database="kammarcials")
            self.con.autocommit = True
            self.cur = self.con.cursor(dictionary=True)

            app.logger.info("Connection Successful")
        except Exception as e:
            app.logger.error(f"Error during connection: {e}")

    def login_model(self, data):
        try:
            decoded_data = data
            encrypted_password = encryption.encrypt(decoded_data['password'])
            self.cur.execute("SELECT id, age FROM users WHERE username = %s AND password = %s",
                             (decoded_data['username'], encrypted_password))

            result = self.cur.fetchall()
            if result:
                user_id = result[0]['id']  # Access the 'id' field of the first row
                user_age = result[0]['age']  # Access the 'age' field of the first row
                app.logger.info(f"Successful login for user: {data['username']}")

                # Store user_id & age in the session
                session['user_id'] = user_id
                session['age'] = user_age
                return make_response(
                    {"message": "Login successful", "username": decoded_data['username'], "user_id": user_id}, 200)
            else:
                app.logger.warning(f"Invalid login attempt for user: {decoded_data['username']}")
                return make_response({"message": "Invalid username or password"}, 201)
        except Exception as e:
            app.logger.error(f"Error in login_model: {e}")
            return make_response({"message": f"An error occurred while processing your request to Login: {e}"}, 500)

    def google_login_model(self, data):
        try:
            email_to_check = data['email']
            query = "SELECT id, age FROM google_users WHERE email = %s;"
            self.cur.execute(query, (email_to_check,))
            result = self.cur.fetchall()

            # Check if the email is found
            if result:
                user_id, user_age = result[0]['id'], result[0]['age']  # Unpack the tuple
                app.logger.info(f"Successful login for user: {data['email']}")

                # Store user_id & age in the session
                session['user_id'] = user_id
                session['age'] = user_age
                return make_response(
                    {'status': 1, 'message': 'User found', 'user_id': user_id, 'age': user_age}, 200)
            else:
                return make_response({'status': 2, 'message': 'User not found'}, 200)
        except Exception as e:
            # Handle exceptions (e.g., database connection error, SQL syntax error)
            return make_response({'status': 0, 'message': f'Error: {str(e)}'}, 500)

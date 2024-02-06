import mysql.connector
from security.encryption import Encryption
from flask import make_response
from app import app

import json

encryption = Encryption(key=11)


class Register:
    def __init__(self):
        try:
            self.con = mysql.connector.connect(host="localhost", user='root', password="",
                                               database="kammarcials")
            self.con.autocommit = True
            self.cur = self.con.cursor(dictionary=True)
            app.logger.info("Connection Successful")
        except Exception as e:
            app.logger.error(f"Error during connection: {e}")

    def register_model(self, data):
        try:
            decoded_data = json.loads(data)
            encrypted_password = encryption.encrypt(decoded_data['password'])
            self.cur.execute(
                "INSERT INTO users(username, password, mobile) VALUES(%s, %s, %s)",
                (decoded_data['username'], encrypted_password, decoded_data['mobile']))
            user_id = self.cur.lastrowid  # Get the ID of the last inserted row
            app.logger.info(f"Added user with ID {user_id}: {data}")
            return make_response({"message": "User registered successfully", "user_id": user_id}, 201)
        except Exception as e:
            app.logger.error(f"Error in register_model: {e}")
            return make_response({"message": f"An error occurred while processing your request to register: {e}"}, 500)
import mysql.connector
from flask import make_response, session
from app import app


class Query:
    def __init__(self):
        try:
            self.con = mysql.connector.connect(host="localhost", user='root', password="",
                                               database="kammarcials")
            self.con.autocommit = True
            self.cur = self.con.cursor(dictionary=True)

            app.logger.info("Connection Successful")
        except Exception as e:
            app.logger.error(f"Error during connection: {e}")

    def user_query_model(self, data):
        try:
            self.cur.execute(
                "INSERT INTO user_queries(email, name, user_id, query) VALUES(%s, %s, %s, %s)",
                (data['email'], data['name'], session.get('user_id'), data['query'])
            )
            app.logger.info(f"User query received from {session.get('user_id')}")
            return make_response({"message": "User query received successfully"}, 200)
        except Exception as e:
            app.logger.error(f"Error in user_query_model: {e}")
            return make_response({"message": f"An error occurred while processing your request to register: {e}"}, 500)

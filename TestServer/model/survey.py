import mysql.connector
from flask import make_response
from app import app


class Survey:
    def __init__(self):
        try:
            self.con = mysql.connector.connect(host="localhost", user='root', password="",
                                               database="kammarcials")
            self.con.autocommit = True
            self.cur = self.con.cursor(dictionary=True)

            app.logger.info("Connection Successful")
        except Exception as e:
            app.logger.error(f"Error during connection: {e}")

    def get_survey_model(self):
        try:
            self.cur.execute("SELECT idquestions FROM questions")
            result = self.cur.fetchall()
            if result:
                idquestions = result[0]['idquestions']  # Access the 'id' field of the first row

            # Extract values of "idquestions" from the result


                app.logger.info("Survey questions fetched")
                return make_response({"result": idquestions}, 200)

        except Exception as e:
            app.logger.error(f"Error in survey_model: {e}")
            return make_response({"message": f"An error occurred while processing your request to register: {e}"}, 500)

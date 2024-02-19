import mysql.connector
from flask import make_response, session
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
            # Access user's age from the session
            user_age = session.get('age')

            # Check if user_age is not None before using it in the SQL query
            if user_age is not None:
                self.cur.execute(
                    f"SELECT surveyid, title FROM survey_details WHERE {user_age} > age_lower AND {user_age} < age_upper")
                result = self.cur.fetchall()

                if result:
                    app.logger.info("Survey questions fetched")
                    for ele in result:
                        self.cur.execute(f"select * from survey_status where surveyid = {ele['surveyid']} and userid={session.get('user_id')}")
                        if self.cur.fetchall():
                            result.remove(ele)
                    return make_response({"result": result}, 200)
                else:
                    app.logger.warning("No survey details found.")
                    return make_response({"message": "No survey details found."},
                                         404)  # or any other appropriate response
            else:
                app.logger.warning("User's age not found in session.")
                return make_response({"message": "User's age not found in session."},
                                     404)  # or any other appropriate response

        except Exception as e:
            app.logger.error(f"Error in survey_model: {e}")
            return make_response({"message": f"An error occurred while processing your request to register: {e}"}, 500)

    def get_survey_question_model(self, data):
        try:
            session['surveyid'] = data['surveyid']
            self.cur.execute(f"SELECT * FROM survey WHERE surveyid={data['surveyid']}")
            result = self.cur.fetchall()
            response = []
            if result:
                questions = result[0]  # Access the 'id' field of the first row
                del questions['surveyid']
                app.logger.info(questions)

                for questionid in questions:
                    self.cur.execute(f"SELECT * FROM questions WHERE questionid={questions[questionid]}")
                    database_response = self.cur.fetchall()
                    response.append(database_response)
                    # app.logger.info(response)
                app.logger.info("Survey questions fetched")
                return make_response({"result": response}, 200)

        except Exception as e:
            app.logger.error(f"Error in survey_model: {e}")
            return make_response({"message": f"An error occurred while processing your request to register: {e}"}, 500)

    def survey_submission_model(self, data):
        pass

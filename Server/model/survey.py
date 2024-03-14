import mysql.connector

from flask import make_response, session
from app import *
from datetime import datetime


class Survey:
    def __init__(self):
        try:
            self.con = mysql.connector.connect(host=sql_host, user=sql_user, password=sql_password,
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
                    f"SELECT survey_id, title FROM survey_details WHERE {user_age} > age_lower AND {user_age} < "
                    f"age_upper AND (total - surveys_left) = surveys_done AND surveys_left>{0}"
                )
                result = self.cur.fetchall()

                if result:
                    app.logger.info("Survey questions fetched")
                    for ele in result:
                        self.cur.execute(
                            f"select * from survey_status where survey_id = {ele['survey_id']} and user_id={session.get('user_id')}")
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
            session['survey_id'] = data['survey_id']
            self.cur.execute(f"UPDATE survey_details SET surveys_left = surveys_left - 1, surveys_done = surveys_done "
                             f"+ 1 WHERE survey_id = {session.get('survey_id')}")

            self.cur.execute(f"SELECT * FROM survey WHERE survey_id={data['survey_id']}")
            result = self.cur.fetchall()
            response = []
            if result:
                questions = result[0]  # Access the 'id' field of the first row
                del questions['survey_id']
                app.logger.info(questions)

                for question_id in questions:
                    self.cur.execute(f"SELECT * FROM questions WHERE question_id={questions[question_id]}")
                    database_response = self.cur.fetchall()
                    response.append(database_response)
                    # app.logger.info(response)
                app.logger.info("Survey questions fetched")
                return make_response({"result": response}, 200)

        except Exception as e:
            app.logger.error(f"Error in survey_model: {e}")
            return make_response({"message": f"An error occurred while processing your request to register: {e}"}, 500)

    def survey_submission_model(self, data):
        try:
            if data['response_status'] == 'incomplete':
                self.cur.execute(
                    f"UPDATE survey_details SET surveys_left = surveys_left + 1, surveys_done = surveys_done - 1 "
                    f"WHERE survey_id = {session.get('survey_id')}")
            # Prepare SQL query to insert a record into the survey_response table
            sql = ("INSERT INTO response_detail (time, survey_id, user_id, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, "
                   "q11, q12, response_status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
            # Execute the SQL query with the data from the JSON request
            self.cur.execute(sql, (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), session.get('survey_id'),
                                   session.get('user_id'), data['q1'], data['q2'], data['q3'], data['q4'], data['q5'],
                                   data['q6'], data['q7'], data['q8'], data['q9'], data['q10'], data['q11'],
                                   data['q12'], data['response_status']))

            self.cur.execute(f"INSERT INTO survey_status (user_id, survey_id, status) VALUES (%s, %s, %s)",
                             (session.get('user_id'), session.get('survey_id'), data['response_status']))
            app.logger.info(session.get('user_id'))
            return make_response({'message': 'Survey submitted successfully'}, 200)
        except Exception as e:
            app.logger.error(f"Error in survey_model: {e}")
            return make_response({'error': str(e)}), 500

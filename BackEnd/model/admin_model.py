import mysql.connector
from flask import make_response
import logging
from controller.error_controller import AppLogger

# Create a logger instance for your module or script
logger_admin = AppLogger()


class Admin:
    def __init__(self):
        try:
            self.con = mysql.connector.connect(host="localhost", user='root', password="",
                                               database="kammarcials")
            self.con.autocommit = True
            self.cur = self.con.cursor(dictionary=True)
            logger_admin.log_info("Connection Successful")
        except Exception as e:
            logger_admin.log_error(f"Error during connection: {e}")

    def admin_add_question_model(self, data):
        try:
            self.cur.execute(
                f"INSERT INTO questions(question, option_a, option_b, option_c, option_d) VALUES('{data['question']}', '{data['option_a']}', '{data['option_b']}', '{data['option_c']}', '{data['option_d']}')")
            logger_admin.log_info(f"Added user: {data}")
            return make_response({"message": "Question added successfully"}, 201)
        except Exception as e:
            logger_admin.log_error(f"Error in user_add_question_model: {e}")
            return make_response({"message": f"An error occurred while processing your request to add question : {e}"},
                                 500)

    def admin_get_all_question_model(self, data):
        try:
            self.cur.execute(f"SELECT * FROM questions WHERE adminid={data['id']}")
            result = self.cur.fetchall()
            if len(result) > 0:
                res = make_response(result, 200)
                res.headers['Access-Control-Allow-Origin'] = "*"
                return res
            else:
                return make_response({"message": "No data found"}, 204)
        except Exception as e:
            logger_admin.log_error(f"Error in admin_get_all_question_model: {e}")
            return make_response(
                {"message": f"An error occurred while processing your request to get all questions : {e}"}, 500)

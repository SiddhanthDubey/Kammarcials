import mysql.connector
from flask import make_response
import logging


class AppLogger:
    def __init__(self, log_file='dev.log'):
        logging.basicConfig(filename=log_file, level=logging.INFO)
        self.logger = logging.getLogger()

    def log_info(self, message):
        self.logger.info(message)

    def log_error(self, message):
        self.logger.error(message)


# Create a logger instance for your module or script
logger_dev = AppLogger()


class Dev:
    def __init__(self):
        try:
            self.con = mysql.connector.connect(host="localhost", user='root', password="",
                                               database="kammarcials")
            self.con.autocommit = True
            self.cur = self.con.cursor(dictionary=True)
            logger_dev.log_info("Connection Successful")
        except Exception as e:
            logger_dev.log_error(f"Error during connection: {e}")

    def dev_add_question_model(self, data):
        try:
            self.cur.execute(
                f"INSERT INTO questions(question, option_a, option_b, option_c, option_d) VALUES('{data['question']}', '{data['option_a']}', '{data['option_b']}', '{data['option_c']}', '{data['option_d']}')")
            logger_dev.log_info(f"Added user: {data}")
            return make_response({"message": "Question added successfully"}, 201)
        except Exception as e:
            logger_dev.log_error(f"Error in user_add_question_model: {e}")
            return make_response({"message": f"An error occurred while processing your request to add question : {e}"},
                                 500)

    def dev_get_all_question_model(self, data):
        try:
            self.cur.execute(f"SELECT * FROM questions WHERE devid={data['id']}")
            result = self.cur.fetchall()
            if len(result) > 0:
                res = make_response(result, 200)
                res.headers['Access-Control-Allow-Origin'] = "*"
                return res
            else:
                return make_response({"message": "No data found"}, 204)
        except Exception as e:
            logger_dev.log_error(f"Error in dev_get_all_question_model: {e}")
            return make_response(
                {"message": f"An error occurred while processing your request to get all questions : {e}"}, 500)

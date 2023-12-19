import mysql.connector
from flask import make_response
import logging
from controller.error_controller import AppLogger

'''
# Configure the logging settings
logging.basicConfig(
    level=logging.DEBUG,  # Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Define the log message format
    #filename='admin.log',  # Specify the log file
    filemode='w'  # Set the file mode ('w' for write, 'a' for append)
)
'''
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
        pass

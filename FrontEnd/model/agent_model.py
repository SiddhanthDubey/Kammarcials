import mysql.connector
from flask import make_response
import logging
from controller.error_controller import AppLogger

'''
# Configure the logging settings
logging.basicConfig(
    level=logging.DEBUG,  # Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Define the log message format
    #filename='agent.log',  # Specify the log file
    filemode='w'  # Set the file mode ('w' for write, 'a' for append)
)
'''
# Create a logger instance for your module or script
logger_agent = AppLogger()


class Agent:
    def __init__(self):
        try:
            self.con = mysql.connector.connect(host="localhost", user='root', password="",
                                               database="repnovation")
            self.con.autocommit = True
            self.cur = self.con.cursor(dictionary=True)
            logger_agent.log_info("Connection Successful")
        except Exception as e:
            logger_agent.log_error(f"Error during connection: {e}")

    def agent_getall_model(self):
        try:
            self.cur.execute('SELECT * FROM users WHERE status = "pending" or status = "alloted"')
            result = self.cur.fetchall()
            if len(result) > 0:
                res = make_response(result, 200)
                res.headers['Access-Control-Allow-Origin'] = "*"
                return res
            else:
                return make_response({"message": "No data found"}, 204)
        except Exception as e:
            logger_agent.log_error(f"Error in agent_getall_model: {e}")
            return make_response({"message": f"An error occurred while processing your request to get user info to agent : {e}"}, 500)

    def agent_apply_model(self, data):
        try:
            qry = f"UPDATE users SET status='alloted' WHERE id='{data['id']}'"
            self.cur.execute(qry)

            self.cur.execute(f"select * from users where id='{data['id']}'")
            result = self.cur.fetchall()
            result = result[0]
            self.cur.execute(
                f"INSERT INTO repnovation.agent(name, address, phone, appliances, status) VALUES('{result['name']}', '{result['address']}', '{result['phone']}', '{result['appliances']}', '{result['status']}')")

            return make_response({"message": "You have applied successfully"}, 201)
        except Exception as e:
            logger_agent.log_error(f"Error in agent_apply_model: {e}")
            return make_response({"message": f"An error occurred while processing your request to apply : {e}"}, 500)

    def agent_apply_history_model(self):
        try:
            self.cur.execute('SELECT * FROM agent WHERE status="completed" or status="alloted"')
            result = self.cur.fetchall()
            if len(result) > 0:
                res = make_response(result, 200)
                res.headers['Access-Control-Allow-Origin'] = "*"
                return res
            else:
                return make_response({"message": "No data found"}, 204)
        except Exception as e:
            logger_agent.log_error(f"Error in agent_apply_history_model: {e}")
            return make_response({"message": f"An error occurred while processing your request to get history : {e}"}, 500)

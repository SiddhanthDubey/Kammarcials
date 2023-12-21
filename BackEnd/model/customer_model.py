import mysql.connector
from flask import make_response
import logging
from controller.error_controller import AppLogger

# Create a logger instance for your module or script
logger_customer = AppLogger()


class Customer:
    def __init__(self):
        try:
            self.con = mysql.connector.connect(host="localhost", user='root', password="",
                                               database="kammarcials")
            self.con.autocommit = True
            self.cur = self.con.cursor(dictionary=True)
            logger_customer.log_info("Connection Successful")
        except Exception as e:
            logger_customer.log_error(f"Error during connection: {e}")

    def user_update_profile_model(self, data):
        try:
            qry = "UPDATE users SET "
            for key in data:
                qry += f"{key}='{data[key]}', "
            qry = qry[:-2] + f" WHERE id={data['id']}"
            self.cur.execute(qry)

            if self.cur.rowcount > 0:
                logger_customer.log_info(f"Updated user with ID: {id}")
                return make_response({"message": "User updated successfully"}, 201)
            else:
                return make_response({"message": "Nothing to update"}, 202)
        except Exception as e:
            logger_customer.log_error(f"Error in user_update_model: {e}")
            return make_response({"message": f"An error occurred while processing your request to update : {e}"}, 500)

    def user_get_profile_model(self, data):
        try:
            self.cur.execute(f"SELECT * FROM users WHERE id={data['id']}")
            result = self.cur.fetchall()
            if len(result) > 0:
                res = make_response(result, 200)
                res.headers['Access-Control-Allow-Origin'] = "*"
                return res
            else:
                return make_response({"message": "No data found"}, 204)
        except Exception as e:
            logger_customer.log_error(f"Error in user_get_profile_model: {e}")
            return make_response(
                {"message": f"An error occurred while processing your request to get user profile: {e}"}, 500)

    def user_delete_profile_model(self, data):
        try:
            self.cur.execute(
                f"DELETE FROM users WHERE id = {data['id']}")
            if self.cur.rowcount > 0:
                logger_customer.log_info(f"Deleted user with ID: {data['id']}")
                return make_response({"message": "Deleted Successfully"}, 200)
            else:
                return make_response({"message": "Nothing is deleted"}, 202)
        except Exception as e:
            logger_customer.log_error(f"Error in user_delete_model: {e}")
            return make_response(
                {"message": f"An error occurred while processing your request to delete profile : {e}"}, 500)

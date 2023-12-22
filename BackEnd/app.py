import logging
import threading
import time

from flask import Flask
from flask import request, make_response

from model.coupon_model import Coupon
from model.customer_model import Customer
from model.dev_model import Dev
from model.login_reg_model import Login, Register


class AppLogger:
    def __init__(self, log_file='app.log'):
        logging.basicConfig(filename=log_file, level=logging.INFO)
        self.logger = logging.getLogger()

    def log_info(self, message):
        self.logger.info(message)

    def log_error(self, message):
        self.logger.error(message)


app = Flask(__name__)
# Configure the logging settings

# Create a logger instance for your module or script
logger_controller = AppLogger()

user = Customer()
dev = Dev()
login = Login()
register = Register()
coupon = Coupon()


@app.route("/login", methods=["GET"])
def login_controller():
    try:
        return login.login_model(request.form)
    except Exception as e:
        logger_controller.log_error(f"Error in login_controller: {e}")
        return make_response({"message": "An error occurred while processing your request"}, 500)


@app.route("/register", methods=["GET", "POST"])
def register_controller():
    try:
        return register.register_model(request.form)
    except Exception as e:
        logger_controller.log_error(f"Error in login_controller: {e}")
        return make_response({"message": "An error occurred while processing your request"}, 500)


@app.route("/dev/addquestion", methods=["POST"])
def dev_add_question_controller():
    try:
        return dev.dev_add_question_model(request.form)
    except Exception as e:
        logger_controller.log_error(f"Error in admin_add_question_controller: {e}")
        return make_response({"message": "An error occurred while processing your request"}, 500)


@app.route("/dev/getallquestions", methods=['GET'])
def dev_get_all_question_controller():
    try:
        dev.dev_get_all_question_model(request.form)
    except Exception as e:
        logger_controller.log_error(f"Error in admin_get_all_question_controller: {e}")
        return make_response({"message": "An error occurred while processing your request"}, 500)


@app.route("/user/profile", methods=['GET'])
def user_get_profile_controller():
    try:
        return user.user_get_profile_model(request.form)
    except Exception as e:
        logger_controller.log_error(f"Error in user_get_profile_controller: {e}")
        return make_response({"message": "An error occurred while processing your request to get profile"}, 500)


@app.route("/user/delete", methods=['GET', 'PUT'])
def user_delete_profile_controller():
    try:
        return user.user_delete_profile_model(request.form)
    except Exception as e:
        logger_controller.log_error(f"Error in user_delete_profile_controller: {e}")
        return make_response({"message": "An error occurred while processing your request to delete profile"}, 500)


@app.route("/user/profileupdate", methods=['GET', 'PUT'])
def user_update_profile_controller():
    try:
        return user.user_update_profile_model(request.form)
    except Exception as e:
        logger_controller.log_error(f"Error in user_delete_profile_controller: {e}")
        return make_response({"message": "An error occurred while processing your request to delete profile"}, 500)

'''
def update_coupon_count():
    while True:
        try:
            # Query the SQL database to get the number of users
            num_users = coupon.get_user_coupon_count_from_database()  # Replace this with your actual database query

            # Log the number of users (you can customize this part)
            logger_controller.log_info(f"Number of users: {num_users}")

            # Sleep for 10 seconds before the next iteration
            time.sleep(10)
        except Exception as e:
            # Log any errors that occur during the process
            logger_controller.log_error(f"Error in update_coupon_count: {e}")
            time.sleep(10)  # Sleep even if there's an error to avoid continuous retries


# Start the thread for updating user count
update_coupon_thread = threading.Thread(target=update_coupon_count())
update_coupon_thread.start()'''

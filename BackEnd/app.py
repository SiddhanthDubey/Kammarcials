from controller.error_controller import AppLogger
from flask import Flask
# dont import here, import user_controller below app = Flask declaration
app = Flask(__name__)

from flask import request, send_file, make_response


from model.customer_model import Customer
from model.admin_model import Admin
from model.login_reg_model import Login, Register

# Configure the logging settings

# Create a logger instance for your module or script
logger_controller = AppLogger()

user = Customer()
admin = Admin()
login = Login()
register = Register()


@app.route("/login", methods=["GET", "POST"])
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


@app.route("/admin/addquestion", methods=["POST"])
def admin_add_question_controller():
    try:
        return admin.admin_add_question_model(request.form)
    except Exception as e:
        logger_controller.log_error(f"Error in admin_add_question_controller: {e}")
        return make_response({"message": "An error occurred while processing your request"}, 500)


@app.route("/admin/getallquestions", methods=['GET'])
def admin_get_all_question_controller():
    try:
        return admin.admin_get_all_question_model(request.form)
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


@app.route("/user/delete", methods=['PUT'])
def user_delete_profile_controller():
    try:
        return user.user_delete_profile_model(request.form)
    except Exception as e:
        logger_controller.log_error(f"Error in user_delete_profile_controller: {e}")
        return make_response({"message": "An error occurred while processing your request to delete profile"}, 500)
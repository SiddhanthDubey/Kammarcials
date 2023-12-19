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

customer = Customer()
admin = Admin()
login = Login()
register = Register()

@app.route("/user/getQuestionHistory")
def user_getall_controller():
    try:
        return customer.user_getall_model()
    except Exception as e:
        logger_controller.log_error(f"Error in user_getList_controller: {e}")
        return make_response({"message": "An error occurred while processing your request"}, 500)

@app.route("/user/addone", methods=["POST"])
def user_addone_controller():
    try:
        return customer.user_addone_model(request.form)
    except Exception as e:
        logger_controller.log_error(f"Error in user_addone_controller: {e}")
        return make_response({"message": "An error occurred while processing your request"}, 500)

@app.route("/user/update", methods=["PUT"])
def user_update_controller():
    try:
        return customer.user_update_model(request.form)
    except Exception as e:
        logger_controller.log_error(f"Error in user_update_controller: {e}")
        return make_response({"message": "An error occurred while processing your request"}, 500)

@app.route("/user/delete", methods=["DELETE"])
def user_delete_controller():
    try:
        return customer.user_delete_model(request.form)
    except Exception as e:
        logger_controller.log_error(f"Error in user_delete_controller: {e}")
        return make_response({"message": "An error occurred while processing your request"}, 500)

@app.route("/admin/getall")
def admin_getall_controller():
    try:
        return admin.admin_getall_model()
    except Exception as e:
        logger_controller.log_error(f"Error in admin_getall_controller: {e}")
        return make_response({"message": "An error occurred while processing your request"}, 500)

@app.route("/admin/apply", methods=["PUT"])
def admin_apply_controller():
    try:
        return admin.admin_apply_model(request.form)
    except Exception as e:
        logger_controller.log_error(f"Error in admin_apply_controller: {e}")
        return make_response({"message": "An error occurred while processing your request"}, 500)

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



from app import app
from flask import request, make_response
from model.register import Register

register = Register()


@app.route("/google_register", methods=["POST"])
def google_register_controller():
    try:
        # data = json.loads(request.data.decode("utf-8"))
        data = request.form
        result = register.google_register_model(data)
        app.logger.info("User registration successful")  # Add an appropriate log message
        return result
    except Exception as e:
        app.logger.error(f"Error in google_register_controller: {str(e)}")
        return make_response({"message": "An error occurred while processing your request"}, 500)


@app.route("/register", methods=["POST"])
def register_controller():
    try:
        # data = json.loads(request.data.decode("utf-8"))
        data = request.form
        result = register.register_model(data)
        app.logger.info("User registration successful")  # Add an appropriate log message
        return result
    except Exception as e:
        app.logger.error(f"Error in register_controller: {str(e)}")
        return make_response({"message": "An error occurred while processing your request"}, 500)
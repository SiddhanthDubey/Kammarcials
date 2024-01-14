from app import app
from flask import request, make_response
from model.login import Login

login = Login()


@app.route("/login", methods=["POST"])
def login_controller():
    try:
        result = login.login_model(request.data)
        app.logger.info("Login successful")  # Add an appropriate log message
        return result
    except Exception as e:
        app.logger.error(f"Error in login_controller: {str(e)}")
        return make_response({"message": "An error occurred while processing your request"}, 500)

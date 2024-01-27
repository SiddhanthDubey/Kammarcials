from app import app
from flask import request, make_response
from model.register import Register

register = Register()

@app.route("/register", methods=["POST"])
def register_controller():
    try:
        result = register.register_model(request.data)
        app.logger.info("User registration successful")  # Add an appropriate log message
        return result
    except Exception as e:
        app.logger.error(f"Error in register_controller: {str(e)}")
        return make_response({"message": "An error occurred while processing your request"}, 500)

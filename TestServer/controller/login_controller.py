from flask import Flask, session, abort, redirect, request, make_response, jsonify

from app import app
from model.login import Login

# import threading

# thread_event = threading.Event()
login = Login()


@app.route("/login", methods=["POST"])
def login_controller():
    try:
        result = login.login_model(request.form)
        app.logger.info("Login successful")

        return result
    except Exception as e:
        app.logger.error(f"Error in login_controller: {str(e)}")
        return make_response({"message": "An error occurred while processing your request"}, 500)


@app.route("/validate", methods=["POST"])
def google_login_controller():
    try:
        result = login.google_login_model(request.form)
        app.logger.info("Login successful")

        return result
    except Exception as e:
        app.logger.error(f"Error in login_controller: {str(e)}")
        return make_response({"message": "An error occurred while processing your request"}, 500)


@app.route("/logout", methods=['GET'])
def logout_controller():
    try:
        session.clear()
        return make_response({"message": f"Logout"},
                             200)  # Redirect to the home page or any other desired page after logout
    except Exception as e:
        app.logger.error(f"Error in logout_controller: {e}")
        return make_response({"message": f"An error occurred while processing your request to Logout: {e}"}, 500)

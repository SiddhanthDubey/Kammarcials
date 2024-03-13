from flask import session, request, make_response
from app import app
from model.login import Login

login = Login()


@app.route("/login", methods=["POST"])
def login_controller():
    try:
        # data = json.loads(request.data.decode("utf-8"))
        data = request.form
        result = login.login_model(data)
        return result
    except Exception as e:
        app.logger.error(f"Error in login_controller: {str(e)}")
        return make_response({"message": "An error occurred while processing your request"}, 500)


@app.route("/validate", methods=["POST"])
def google_login_controller():
    try:
        # data = json.loads(request.data.decode("utf-8"))
        data = request.form
        result = login.google_login_model(data)

        return result
    except Exception as e:
        app.logger.error(f"Error in login_controller: {str(e)}")
        return make_response({"message": "An error occurred while processing your request"}, 500)


@app.route("/logout", methods=['GET'])
def logout_controller():
    try:
        session.clear()
        return make_response({"message": f"Logout"}, 200)
    except Exception as e:
        app.logger.error(f"Error in logout_controller: {e}")
        return make_response({"message": f"An error occurred while processing your request to Logout: {e}"}, 500)

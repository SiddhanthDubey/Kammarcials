# app.py
from controller.coupon_controller import coupon
import os
import pathlib
import requests
from flask import Flask, session, abort, redirect, request, make_response, jsonify
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
from pip._vendor import cachecontrol
import google.auth.transport.requests
from app import app
from model.login import Login
import threading

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
GOOGLE_CLIENT_ID = "351086737071-er5ao5sh875snfi6ec5creortvmp6h29.apps.googleusercontent.com"
client_secrets_file = os.path.join(pathlib.Path(__file__).parent, "client_secret.json")

flow = Flow.from_client_secrets_file(
    client_secrets_file=client_secrets_file,
    scopes=["https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email",
            "openid"],
    redirect_uri="http://127.0.0.1:5000/callback"
)

thread_event = threading.Event()
login = Login()


@app.route("/login", methods=["POST"])
def login_controller():
    try:
        result = login.login_model(request.data)
        app.logger.info("Login successful")

        return result
    except Exception as e:
        app.logger.error(f"Error in login_controller: {str(e)}")
        return make_response({"message": "An error occurred while processing your request"}, 500)


@app.route("/google_login")
def google_login_controller():
    authorization_url, state = flow.authorization_url()
    #session['state'] = state

    response_data = {"url": authorization_url}
    response = make_response(jsonify(response_data), 200)
    response.headers["Content-Type"] = "application/json"
    return response


@app.route("/callback")
def google_login_callback_controller():
    flow.fetch_token(authorization_response=request.url)

    #if not session['state'] == request.args['state']:
        #abort(500)

    credentials = flow.credentials
    request_session = requests.session()
    cached_session = cachecontrol.CacheControl(request_session)
    token_request = google.auth.transport.requests.Request(session=cached_session)

    id_info = id_token.verify_oauth2_token(
        id_token=credentials._id_token,
        request=token_request,
        audience=GOOGLE_CLIENT_ID,
        clock_skew_in_seconds=10
    )

    session["google_id"] = id_info.get("sub")
    session["name"] = id_info.get("name")
    return redirect("/")


@app.route("/logout", methods=['GET'])
def logout_controller():
    try:

        return make_response({"message": f"Logout"}, 200)  # Redirect to the home page or any other desired page after logout
    except Exception as e:
        app.logger.error(f"Error in logout_controller: {e}")
        return make_response({"message": f"An error occurred while processing your request to Logout: {e}"}, 500)

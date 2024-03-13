from flask import Flask
from flask_cors import CORS
from flask_session import Session
from logger.server_logger import setup_logger

import json

app_settings = json.load(open('config.json'))

sql_host = app_settings['sql_config']['host']
sql_user = app_settings['sql_config']['user']
sql_password = app_settings['sql_config']['password']

app = Flask(__name__)
CORS(app)

# Set your secret key
app.config['SECRET_KEY'] = app_settings['app_config']['SECRET_KEY']

# Configure Flask-Session
app.config['SESSION_TYPE'] = app_settings['app_config']['SESSION_TYPE']  # Use filesystem as the session storage
app.config['SESSION_PERMANENT'] = app_settings['app_config']['SESSION_PERMANENT']  # Session is not permanent
app.config['SESSION_USE_SIGNER'] = app_settings['app_config']['SESSION_USE_SIGNER']  # Sign session cookie for security
app.config['SESSION_KEY_PREFIX'] = app_settings['app_config']['SESSION_KEY_PREFIX']  # Prefix for session keys
Session(app)

# Set up the logger
setup_logger(app)

from controller import login_controller
from controller import register_controller
from controller import survey_controller
from controller import general_controller


@app.route('/')
def welcome():
    app.logger.info("Welcome endpoint accessed")
    return "Hello World"


@app.route('/home')
def home_page():
    app.logger.info("Home page accessed")
    return "This is the home page"


'''
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
'''

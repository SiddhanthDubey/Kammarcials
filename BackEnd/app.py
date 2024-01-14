from flask import Flask
from flask_cors import CORS
from flask import Flask
from flask_cors import CORS
from logger.server_logger import setup_logger

app = Flask(__name__)
CORS(app)

# Set up the logger
setup_logger(app)

@app.route('/')
def welcome():
    app.logger.info("Welcome endpoint accessed")
    return "Hello World"

@app.route('/home')
def home_page():
    app.logger.info("Home page accessed")
    return "This is the home page"

# Import controllers after logger setup
from controller import login_controller
from controller import register_controller

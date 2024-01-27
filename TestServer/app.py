from flask import Flask
from flask_cors import CORS
from flask_session import Session
from logger.server_logger import setup_logger


app = Flask(__name__)
CORS(app)

# Set your secret key
app.config['SECRET_KEY'] = '9etRufraqe'

# Configure Flask-Session
app.config['SESSION_TYPE'] = 'filesystem'  # Use filesystem as the session storage
app.config['SESSION_PERMANENT'] = False  # Session is not permanent
app.config['SESSION_USE_SIGNER'] = True  # Sign session cookie for security
app.config['SESSION_KEY_PREFIX'] = 'kammarcials_'  # Prefix for session keys
Session(app)

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
from controller import survey_controller
#from controller import coupon_controller

#coupon = coupon_controller.Coupon()


def run_flask_app():
    app.run(debug=True, use_reloader=False, port=5000, host='127.0.0.1')

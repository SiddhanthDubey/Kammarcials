from flask import Flask
# dont import here, import user_controller below app = Flask declaration
app = Flask(__name__)

@app.route('/')
def welcome():
    return "Hello World"

@app.route('/home')
def home_page():
    return "this is home page"

#or u can import by using below
from controller import *


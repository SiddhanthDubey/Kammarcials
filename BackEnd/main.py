from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World'


@app.route('/add/<int:a>,<int:b>')
def add(a, b):
    z = a + b
    result = {
        "number": [a, b],
        "result": z
    }

    return jsonify(result)


app.run(debug=True)

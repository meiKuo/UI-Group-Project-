from imghdr import what
from unittest import result
from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
from itsdangerous import json
from numpy import result_type
app = Flask(__name__)

# add to data
data = {
    "1": {
        "mushroom": "1"
    },
    "2": {
        "mushroom": "2"
    },
    "3": {
        "mushroom": "3"
    },
}

current_id = 10

# ROUTES
@app.route('/')
def homepage():
    top_three = [data["1"], data["2"], data["3"]]
    return render_template('homepage.html', data=top_three)

if __name__ == '__main__':
    app.run(debug=True)

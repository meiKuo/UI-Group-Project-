from flask import Flask
from flask import render_template
from flask import Response, request, jsonify, request
app = Flask(__name__)

from data import questions
from data import mushrooms

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

@app.route('/game', methods=['GET', 'POST'])
def game():
    if request.method == 'POST':
        id = request.args.get('id')
        print(id)
        return mushrooms[id]

    return render_template('game.html', questions=questions)

if __name__ == '__main__':
    app.run(debug=True)

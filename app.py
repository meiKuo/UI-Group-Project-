import json
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

lives = 4
hunger = 0
cur_question = 1

score = 0

# ROUTES
@app.route('/')
def homepage():
    top_three = [data["1"], data["2"], data["3"]]
    return render_template('homepage.html', data=top_three)

@app.route('/game/<q_idx>', methods=['GET', 'POST'])
def game(q_idx):
    global lives
    global hunger
    global cur_question

    if int(q_idx) == 1:
        lives = 4
        hunger = 0

    if int(q_idx) > len(questions):
        return "Error: Out of question range."

    cur_question = int(q_idx)

    m_id = questions[cur_question - 1]["mushroom"]
    print(mushrooms[m_id])

    game_params = {
        "lives": lives,
        "hunger": hunger,
        "question": questions[cur_question - 1],
        "mushroom": mushrooms[m_id]
    }

    return render_template('game.html', **game_params )

@app.route('/update', methods=['POST'])
def update():
    global lives
    global score
    global hunger
    idx = request.get_json()

    if idx != questions[cur_question - 1]["correct_choice"]:
        if lives > 0:
            lives -= 1
    else:
        score += 1

    user_stats = {
        "lives": lives,
        "hunger": hunger,
        "score": score,
    }
    return jsonify(user_stats)
if __name__ == '__main__':
    app.run(debug=True)

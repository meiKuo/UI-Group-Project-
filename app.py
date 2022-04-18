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
    global score

    end = False 

    if int(q_idx) == 1:
        lives = 4
        hunger = 0

    cur_question = int(q_idx)

    if int(q_idx) == len(questions) + 1:
        end = True

    if int(q_idx) > len(questions) + 1:
        return "Error: Out of question range."

    cur_question = cur_question if cur_question <= len(questions) else 1
    m_id = questions[cur_question - 1]["mushroom"]

    game_params = {
        "lives": lives,
        "hunger": hunger,
        "score": score,
        "end": end,
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

    correct = idx == questions[cur_question - 1]["correct_choice"]

    if not correct:
        if lives > 0:
            lives -= 1
    else:
        score += 1
    
    hunger += 10

    user_stats = {
        "lives": lives,
        "hunger": hunger,
        "score": score,
    }

    return jsonify(user_stats)

@app.route('/lesson1')
def lesson():
    return render_template('lesson1_compare.html', data=data)

@app.route('/lesson2')
def lesson2():
    return render_template('lesson2_present.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)

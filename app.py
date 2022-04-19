import json
from flask import Flask
from flask import render_template
from flask import Response, request, jsonify, request
app = Flask(__name__)

from data import questions
from data import mushrooms
from data import lessons

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


#essons = ["Differentiating edible from poisonous mushrooms","Psychedelic Mushrooms"]


health = 100
lives = 3
hunger = 0
cur_question = 1

score = 0

# ROUTES
@app.route('/')
def homepage():
    lesson_name1 = lessons["1"]
    lesson_name2 = lessons["2"]
    print(lesson_name1)
    return render_template('homepage.html', lesson_name1=lesson_name1, lesson_name2=lesson_name2)

@app.route('/game/<q_idx>', methods=['GET', 'POST'])
def game(q_idx):
    global lives
    global health
    global hunger
    global cur_question

    if int(q_idx) == 1:
        health = 100
        lives = 3
        hunger = 0

    if int(q_idx) == len(questions) + 1:
        return "You've reached the end of the quiz."

    if int(q_idx) > len(questions):
        return "Error: Out of question range."

    cur_question = int(q_idx)

    m_id = questions[cur_question - 1]["mushroom"]
    print(mushrooms[m_id])

    game_params = {
        "lives": lives,
        "health": health,
        "hunger": hunger,
        "question": questions[cur_question - 1],
        "mushroom": mushrooms[m_id]
    }

    return render_template('game.html', **game_params )

@app.route('/update', methods=['POST'])
def update():
    global lives
    global health
    global score
    global hunger
    idx = request.get_json()

    correct = idx == questions[cur_question - 1]["correct_choice"]

    if not correct:
        if lives > 0:
            lives -= 1
    else:
        score += 1

    user_stats = {
        "lives": lives,
        "health": health,
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

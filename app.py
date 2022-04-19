import json
from flask import Flask
from flask import render_template
from flask import Response, request, jsonify, request
app = Flask(__name__)

from data import questions, mushrooms, quizMushrooms

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


lessons = ["Differentiating edible from poisonous mushrooms","Psychedelic Mushrooms"]


health = 100
hunger = 0

score = 0

# ROUTES
@app.route('/')
def homepage():
    top_three = [data["1"], data["2"], data["3"]]
    return render_template('homepage.html', data=[top_three, lessons])

@app.route('/game/<path>')
def game(path=None):
    if path == "home":
        return render_template('game_home.html')
    elif path == "main":
        global health
        global hunger
        global quizMushrooms

        # if int(q_idx) == 1:
        #     health = 100
        #     hunger = 0

        # if int(q_idx) == len(questions) + 1:
        #     return "You've reached the end of the quiz."
        #
        # if int(q_idx) > len(questions):
        #     return "Error: Out of question range."

        game_params = {
            "health": health,
            "hunger": hunger,
            "mushrooms": quizMushrooms,
        }

        return render_template('game.html', **game_params)

@app.route('/update', methods=['POST'])
def update():
    global health
    global score
    global hunger
    idx = request.get_json()

    # correct = idx == questions[cur_question - 1]["correct_choice"]

    # if not correct:
    #     if lives > 0:
    #         lives -= 1
    # else:
    #     score += 1

    user_stats = {
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

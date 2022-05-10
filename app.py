import json
from operator import le
from flask import Flask
from flask import render_template
from flask import Response, request, jsonify, request, redirect
app = Flask(__name__)

from data import *

health = 100
hunger = 100

HUNGER_CHANGE = (100 // find_num_edible()) + 1
HEALTH_CHANGE = (100 // find_num_inedible()) + 1

# ROUTES
@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/lessonplans')
def lessonplans():
    global lessons

    def get_mushroom_edible(id):
        return mushrooms[id]["edible"]

    def check_completion(lesson):
        if not "complete" in lesson:
            return False
        
        return lesson["complete"]
    
    def get_num_completed():
        return len([lesson for lesson in lessons.values() if check_completion(lesson)])

    complete = len(lessons) == get_num_completed()

    for lesson in lessons.values():
        lesson["edible"] = get_mushroom_edible(lesson["mushroom"])

    params = {
        "lessons": lessons.values(),
        "complete": complete,
        "num_completed": get_num_completed(),
    }

    return render_template('lesson_plans.html', **params)
@app.route('/game/<path>')
def game(path):
    global health
    global mushrooms
    global quiz

    def reset_game():
        for q in quiz.values():
            q["done"] = False

        global health
        global hunger
        health = 100
        hunger = 100

    def get_remaining_quiz(quiz):
        return [q for q in quiz.values() if not q["done"]]

    if path == "start":
        reset_game()

        game_params = {
            "state": 0,
            "quiz_id": "0",
            "health": health,
            "hunger": hunger,
        }

        return render_template("game.html", **game_params)
    
    remaining_quiz = get_remaining_quiz(quiz)
    if len(remaining_quiz) == 0 or path=="end":
        STATS_DIALOGUE = "".format(health, hunger)
        game_params = {
            "state": 7,
            "quiz_id": "0",
            "hunger": hunger,
            "health": health,
            "dialogue": STATS_DIALOGUE,
        }

        return render_template("game.html", **game_params)

    if path == "map":

        game_params = {
            "displayMap": True,
            "quiz": quiz.values(),
            "quiz_id": "0",
            "state": 1,
            "health": health,
            "hunger": hunger,
        }
        return render_template("game.html", **game_params)

    elif path.isdigit():
        if int(path) < 1 or int(path) > len(quiz.values()):
            return "Error: Invalid quiz id."

        game_params = {
            "displayGameImg": True,
            "displayMap": False,
            "quiz": quiz[path],
            "quiz_id": quiz[path]["id"],
            "state": 2,
            "health": health,
            "hunger": hunger,
        }

        return render_template("game.html", **game_params)

@app.route('/update', methods=['POST'])
def update():
    global health
    global quiz
    global mushrooms
    global hunger

    data = request.get_json()

    def get_mushroom(quiz_id):
        return mushrooms[quiz[quiz_id]["mushroom_id"]]

    mushroom = get_mushroom(data['quiz_id'])

    if data['eat'] and mushroom['edible']:
        # User ate mushroom and mushroom edible
        hunger = max(0, hunger - HUNGER_CHANGE)

    elif data['eat'] and not mushroom['edible']:
        # User ate, not edible
        health = max(0, health - HEALTH_CHANGE)

    elif not data['eat'] and mushroom['edible']:
        # user did not eat, edible
        hunger = min(100, hunger + HUNGER_CHANGE)


    # Else: Did not eat, not edible

    # Mark quiz_id as done
    quiz[data['quiz_id']]["done"] = True

    choice_result = {
        "health": health,
        "hunger": hunger,
        "eat": data['eat'],
        "mushroomName": mushroom["name"],
        "edible": mushroom["edible"],
    }

    return jsonify(choice_result)

@app.route('/lesson/<id>')
def lesson(id):
    global lessons
    global mushrooms

    lesson_id = int(id)
    if lesson_id  > len(lessons.values()) or lesson_id < 1:
        return "Error: Invalid lesson number."

    cur_lesson = lessons[id]
    lessons[id]["complete"] = True
    
    def check_completion(lesson):
        if not "complete" in lesson:
            return False
        
        return lesson["complete"]

    # Get remaining lessons
    def get_next_lesson():
        for lesson in lessons.values():
            if not check_completion(lesson):
                return lesson["lesson_id"]
        
        return "0"

    lesson_params = {
        "lesson_id": id,
        "lesson_name": cur_lesson["lesson_name"],
        "mushroom": mushrooms[cur_lesson["mushroom"]],
        "next": get_next_lesson(),
    }

    if cur_lesson["type"] == "compare":
        lesson_params["compare"] = mushrooms[cur_lesson["compare"]]

    return render_template('lesson_present.html', **lesson_params)


@app.route('/lesson/<lesson_id>/compare/<id1>/<id2>')
def compare(lesson_id, id1, id2):
    global lessons

    mushroom1 = mushrooms[id1]
    mushroom2 = mushrooms[id2]

    lesson_params = {
        "mushroom1": mushroom1,
        "mushroom2" : mushroom2,
        "lesson_id": lesson_id,
    }
    
    return render_template('lesson_compare.html', data=lesson_params)


if __name__ == '__main__':
    app.run(debug=True)

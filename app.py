import json
from flask import Flask
from flask import render_template
from flask import Response, request, jsonify, request, redirect
app = Flask(__name__)

from data import questions, mushrooms, quizMushrooms, lessons

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
hunger = 10

# ROUTES
@app.route('/')
def homepage():
    lesson_name1 = lessons["1"]
    lesson_name3 = lessons["3"]
    print(lesson_name1)
    return render_template('homepage.html', lesson_name1=lesson_name1, lesson_name3=lesson_name3)

@app.route('/game/<path>')
def game(path=None):
    global health
    global hunger
    global quizMushrooms
    global game_params
    global mushrooms

    if path == "home":
        return render_template('game_home.html')
    elif path == "map" and len(quizMushrooms):
        game_params = {
            "health": health,
            "hunger": hunger,
            "mushrooms": quizMushrooms,
        }

        return render_template('game_map.html', **game_params)
    elif len(quizMushrooms) and health > 0:
        print(len(quizMushrooms), health)
        for mush in quizMushrooms:
            if path == mush['id']:
                return render_template('game_ind_mushroom.html', mushroom=mush)
        return 'End of game!'
    else:
        data = {
            'health': health,
            'hunger': hunger,
            'quizMushrooms': quizMushrooms,
        }

        return render_template('end_game.html', data=data)


@app.route('/update', methods=['POST'])
def update():
    global health
    global hunger
    global quizMushrooms
    data = request.get_json()
    print(data)

    if data['choice'] == 'eat' and data['mushroom']['edible']:
        # user ate and mushroom edible
        # reduce hunger and increase health
        if hunger > 10:
            hunger = hunger - 10
        else:
            hunger = 0

        if health < 90:
            health = health + 10
        else:
            health = 100
    elif data['choice'] == 'eat' and not data['mushroom']['edible']:
        # user ate but mushroom not edible
        # reduce health and increase hunger
        if health > 10:
            health = health - 10
        else:
            health = 0
        if hunger < 90:
            hunger = hunger + 10
        else:
            hunger = 100
            health = health - 10
    elif data['choice'] != 'eat':
        # user chose not to eat
        # increase hunger
        if hunger < 90:
            hunger = hunger + 10
        else:
            hunger = 100
            health = health - 10


    quizMushrooms.remove(data['mushroom'])

    user_stats = {
        "health": health,
        "hunger": hunger,
    }

    return jsonify(user_stats)

@app.route('/lesson1')
def lesson():
    mushroom1 = mushrooms["0"]
    mushroom2 = mushrooms["1"]   
    lesson_name1 = lessons["1"]
    return render_template('lesson1_compare.html', mushroom1 = mushroom1, mushroom2 = mushroom2, lesson_name1 = lesson_name1)

@app.route('/lesson2')
def lesson2():
    lesson = lessons["3"]
    mushroom = mushrooms['2']
    return render_template('lesson2_present.html', lesson=lesson, mushroom = mushroom)

if __name__ == '__main__':
    app.run(debug=True)

mushrooms = {
    "0": {
        "id": "0",
        "name": "Black Morel",
        "edible": True,
        "img_url": 'images/morel_1.png',
        "cut_img_url": "images/morel_1.png",
        "features": [
            "Irregularly shaped",
            "Bulging outwards",
            "Wavy and lobed",
            "Hangs freely from the stem"
        ]
    },
    "1": {
        "id": "0",
        "name": "False Morel",
        "edible": True,
        "img_url": 'images/morel_1.png',
        "cut_img_url": "images/morel_1.png",
        "features": [
            "Irregularly shaped",
            "Bulging outwards",
            "Wavy and lobed",
            "Hangs freely from the stem"
        ]
    }
}

# Questions for quiz
quizMushrooms = [
    {
        "id": "0",
        "name": "Black Morel",
        "edible": True,
        "poisonous": False,
        "img_url": 'images/morel_1.png',
        "cut_img_url": "images/morel_open_1.png",
        "features": [
            "Irregularly shaped",
            "Bulging outwards",
            "Wavy and lobed",
            "Hangs freely from the stem"
        ]
    },
    {
        "id": "1",
        "name": "False Morel",
        "edible": False,
        "poisonous": True,
        "img_url": 'images/false_morel_1.png',
        "cut_img_url": "images/false_morel_1.png",
        "features": [
            "Irregularly shaped",
            "Bulging outwards",
            "Wavy and lobed",
            "Hangs freely from the stem"
        ]
    },
    {
        "id": "2",
        "name": "Death Cap",
        "edible": False,
        "poisonous": True,
        "img_url": 'images/death_cap_1.png',
        "cut_img_url": "images/death_cap_1.png",
        "features": [
            "Irregularly shaped",
            "Bulging outwards",
            "Wavy and lobed",
            "Hangs freely from the stem"
        ]
    },
    {
        "id": "3",
        "name": "Destorying Angel",
        "edible": False,
        "poisonous": True,
        "img_url": 'images/destorying_angel_1.png',
        "cut_img_url": "images/destorying_angel_1.png",
        "features": [
            "Irregularly shaped",
            "Bulging outwards",
            "Wavy and lobed",
            "Hangs freely from the stem"
        ]
    },
    {
        "id": "4",
        "name": "Giant Puffball",
        "edible": True,
        "poisonous": False,
        "img_url": 'images/puffball_mushroom_1.png',
        "cut_img_url": "images/puffball_mushroom_open_1.png",
        "features": [
            "Irregularly shaped",
            "Bulging outwards",
            "Wavy and lobed",
            "Hangs freely from the stem"
        ]
    },

]
questions = [
    {
        "id": 1,
        "question": "Hmm, this mushroom looks interesting. Not sure if it's edible. What do you think?",
        "mushroom": "0", # ID from mushrooms[]
        "health_cost": 1,
        "hunger_cost": 0,
        "cut_dialogue": "It looks like the mushroom is hollow from tip to stem.",
        "correct_choice": 0,
    },
    {
        "id": 2,
        "question": "Hmm, this mushroom looks interesting. Not sure if it's edible. What do you think?",
        "mushroom": "0", # ID from mushrooms[]
        "health_cost": 1,
        "hunger_cost": 0,
        "cut_dialogue": "It looks like the mushroom is hollow from tip to stem.",
        "correct_choice": 0,
    }
]

#lessons 
lessons = {
    "1": {
        "lesson_id": "1",
        "lesson_name": "Differentiating Edible and Poisonous Mushrooms", 
        "description": "On the left we have true morel mushrooms and on the right we have false morel mushrooms.",
        "type": "compare", 
        "mushroom1": "0",
        "mushrrom2": "0" , 
    }, 
    "2": {
        "lesson_id": "2",
        "lesson_name": "2Differentiating Edible and Poisonous Mushrooms",
        "description": "On the left we have true morel mushrooms and on the right we have false morel mushrooms.",
        "type": "compare", 
        "mushroom1": "0",
        "mushrrom2": "0" , 
    },
}
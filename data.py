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
    }
}

# Questions for quiz
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

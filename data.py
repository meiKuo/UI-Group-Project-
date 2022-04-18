

mushrooms = {
    "0": {
        "id": 0,
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
        "question": "You've encountered a mushroom! What will you do?",
        "mushroom": "0", # ID from mushrooms[]
        "health_cost": 1,
        "hunger_cost": 0,
        "choices": [
            {
                "text": "Let's eat it!",
                "dialogue": "Yup, you got it.",
            },
            {
                "text": "Nah, it's toxic",
                "dialogue": "Oh no! You ate a super poisonous mushroom."
            }
        ],
        "correct_choice": 0,
    }
]
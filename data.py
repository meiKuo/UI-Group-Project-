mushrooms = {
    "1": {
        "id": "1",
        "name": "Black Morel",
        "edible": True,
        "img_url": 'https://cdn.dribbble.com/users/2860422/screenshots/9385109/media/dc407522c3ef84385e1c7cdcb01d90e6.png?compress=1&resize=400x300',
        "cut_img_url": "images/morel_1.png",
        "features": [
            "Irregularly shaped",
            "Bulging outwards",
            "Wavy and lobed",
            "Hangs freely from the stem"
        ]
    },
    "2": {
        "id": "2",
        "name": "False Morel",
        "edible": False,
        "img_url": 'https://as1.ftcdn.net/v2/jpg/02/94/34/30/1000_F_294343087_4w1GR3vVswC4RoOslk9VxORUxiRb20Rw.jpg',
        "cut_img_url": "images/morel_1.png",
        "features": [
            "Irregularly shaped",
            "Bulging outwards",
            "Wavy and lobed",
            "Hangs freely from the stem"
        ]
    }, 
    "3": {
        "id": "3",
        "name": "Death Cap",
        "edible": False,
        "img_url": 'https://cdn-s-www.bienpublic.com/images/8DF87B22-AADD-4FC0-8FC7-8632C3480795/NW_raw/les-champignons-tels-que-les-quot-psilocybe-semilanceata-quot-sont-inscrits-sur-la-liste-des-stupefiants-depuis-1990-en-france-photo-d-illustration-pixabay-domaine-public-1507911226.jpg',
        "cut_img_url": "images/morel_1.png",
        "features": [
            "Irregularly shaped",
            "Bulging outwards",
            "Wavy and lobed",
            "Hangs freely from the stem"
        ]
    },
    "4": {
        "id": "4",
        "name": "Giant Puffball",
        "edible": True,
        "img_url": 'images/puffball_mushroom_1.png',
        "cut_img_url": "images/puffball_mushroom_open_1.png",
        "features": [
            "Irregularly shaped",
            "Bulging outwards",
            "Wavy and lobed",
            "Hangs freely from the stem"
        ]
    },
    "5": {
        "id": "5",
        "name": "Destorying Angel",
        "edible": False,
        "img_url": 'images/destorying_angel_1.png',
        "cut_img_url": "images/destorying_angel_1.png",
        "features": [
            "Irregularly shaped",
            "Bulging outwards",
            "Wavy and lobed",
            "Hangs freely from the stem"
        ]
    },

}

quiz = {
    "1": {
        "id": "1",
        "mushroom_id": "1",
        "img_url": 'images/morel_1.png',
        "cut_img_url": "images/morel_1.png",
        "done": False
    },
    "2": {
        "id": "2",
        "mushroom_id": "2",
        "img_url": 'images/false_morel_1.png',
        "cut_img_url": "images/false_morel_1.png",
        "done": False
    },
    "3": {
        "id": "3",
        "mushroom_id": "4",
        "img_url": 'images/puffball_mushroom_1.png',
        "cut_img_url": "images/puffball_mushroom_open_1.png",
        "done": False
    },
    "4": {
        "id": "4",
        "mushroom_id": "3",
        "img_url": 'images/death_cap_1.png',
        "cut_img_url": "images/death_cap_1.png",
        "done": False
    }
}


#lessons 
lessons = [
    {
        "lesson_name": "Differentiating Edible and Poisonous Mushrooms", 
        "description": "On the left we have true morel mushrooms and on the right we have false morel mushrooms.",
        "type": "compare", 
        "mushroom1": "0",
        "mushroom2": "1" , 
    }, 
    {
        "lesson_name": "Differentiating Edible and Poisonous Mushrooms",
        "description": "On the left we have true morel mushrooms and on the right we have false morel mushrooms.",
        "type": "compare", 
        "mushroom1": "0",
        "mushroom2": "2" , 
    },
    {
        "lesson_name": "Identifying Psychedelic Mushrooms",
        "description": "There are 227 known and classified species of psychedelic mushrooms.",
        "type": "description", 
        "mushroom1": "2",
    },
]

START_DIALOGUE = """Welcome to wild, wild wilderness. Here we'll test everything you've learned.\n\n 
                    Toxic mushrooms and getting too hungry can decrease your health, so be careful!"""

ON_CHOICE_DIALOGUE = "Hmm, this looks interesting. What will you do?"
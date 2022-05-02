mushrooms = {
    "0": {
        "id": "0",
        "name": "Black Morel",
        "edible": True,
        "img_url": '/static/images/blackmorel.png',
        "cut_img_url": "images/puffball_mushroom_open_1.png",
        "cap": "Scalloped, whitish-grey (sometimes tan) caps",
        "stem": "Pebbly texture",
        "gills": "Conical or oval Attached cap",
        "taste": "Earthy, woodsy, and nutty",
        "color": "Range in color: from cream to black",
        "location": "Found in moist areas and on specific trees like maple, conifers, and oak",
        "inner": "White",
        "description": "Black Morels are unlike most of our common mushrooms. They lack gills, pores, or teeth to drop spores.",
    },
    "1": {
        "id": "1",
        "name": "False Morel",
        "edible": False,
        "img_url": '/static/images/False Morels.png',
        "cut_img_url": "images/puffball_mushroom_open_1.png",
        "cap": "Brain-like or saddle-shaped structure",
        "stem": "Cotton-like white stem when sliced down the middle",
        "gills": "N/A",
        "taste": "N/A",
        "color": "Reddish or a brownish redn",
        "location": "Grow in disturbed soil across North America and Europe.",
        "inner": "White",
        "description": "The False Morel is a Spring mushroom that contains the toxin gyromitrin. Raw or cooked - it can be very toxic, even deadly when enough is consumed.",
    },
    "2": {
        "id": "2",
        "name": "Destroying Angel",
        "edible": False,
        "img_url": '/static/images/destroyingangel.png',
        "cut_img_url": "images/morel_1.png",
        "cap": "Pure white stalks cap",
        "stem": "Pure white stems",
        "gills": "Pure white gills",
        "taste": "N/A",
        "color": "White",
        "location": "Near woodlands or shrubs in suburban lawns/meadows",
        "inner": "White",
        "description": "Destroying angels are among the most toxic known mushrooms. The destroying angel is all white, with a ring on the stalk and a large, saclike cup around the base of the stalk.",
    },
    "3": {
        "id": "3",
        "name": "Giant Puffball",
        "edible": True,
        "img_url": '/static/images/giantpuffball.png',
        "cut_img_url": "images/puffball_mushroom_open_1.png",
        "cap": "Pure white stalks cap",
        "stem": "Pure white stems",
        "gills": "N/A",
        "taste": "Taste rich, earthy, and nutty",
        "color": "White",
        "location": "Found in meadows, fields, and deciduous forests",
        "inner": "White",
        "description":"Giant puffball mushrooms can be found all over the country, but mostly in the midwest from the summer until about October.",
    },
    "4": {
        "id": "4",
        "name": "Chanterelle",
        "img_url": "/static/images/chanterelle.png",
        "cut_img_url": "",
        "edible": True,
        "cap": "Funnel shaped, wavy",
        "stem": "Full stem",
        "gills": "Blunt, gill-like ridges",
        "taste": "Peppery/peachy/apricot",
        "color": "Bright yellow/orange",
        "location": "East and West Coasts",
        "inner": "White internal flesh",
        "description": "Chanterelles are known for their beautiful yellow-orange color, their rarity, and most of all, their flavor.",


        },
    "5": {
        "id": "5",
        "name": "Jack o Lantern",
        "img_url": "/static/images/jackolantern.png",
        "cut_img_url": "",
        "edible": False,
        "cap": "Round, flat",
        "stem": "Hollow stem",
        "gills": "True, sharp gills on stalk",
        "taste": "N/A",
        "color": "Orangy brown",
        "location": "East & West of Rocky Mts",
        "inner": "Orange internal flesh",
        "description": "Jack o' Lantern is a bright orange mushroom that usually grows in dense tufts from the decaying underground roots of trees or from dead stumps.",
        },
    "6": {
        "id": "6",
        "name": "Maitake Mushroom",
        "edible": True,
        "img_url": '/static/images/maitake.png',
        "cut_img_url": "images/puffball_mushroom_open_1.png",
        "cap": "Distinctive shape that resembles mane of a male lion or a pom pom",
        "stem": "Woody stem",
        "gills": "No gills, but leave a white spore print",
        "taste": "Strong earthy, peppery flavor",
        "color": "Brown",
        "location": "Mainly found in the northeast",
        "inner": "White",
        "description": "Maitake” means dancing mushroom in Japanese. The mushroom is said to have gotten its name after people danced with happiness upon finding it in the wild.",

    },
    "7": {
        "id": "7",
        "name": "Oyster Mushroom",
        "edible": True,
        "img_url": '/static/images/oystermushroom.png',
        "cut_img_url": "images/puffball_mushroom_open_1.png",
        "cap": "Scalloped, whitish-grey (sometimes tan) caps",
        "stem": "Woody stem",
        "gills": "White, decurrent gills",
        "taste": "Delicate and savory, with a hint of complexity on the finish",
        "color": "Grayish-brown",
        "location": "Found on dying hardwood trees like oaks, maples, etc especially after it rains",
        "inner": "White",
        "description": "Oyster mushrooms have a white to light brown to a darker brown, funnel-shaped cap, with whitish- yellow gills running up a short off-center stem. The flesh is white.",
    },
    "8": {
        "id": "8",
        "name": "Lion's Mane",
        "edible": True,
        "img_url": '/static/images/lionsmane.png',
        "cut_img_url": "images/puffball_mushroom_open_1.png",
        "cap": "Distinctive shape that resembles mane of a male lion or a pom pom",
        "stem": "Pure white stems",
        "gills": "Instead of gills, this mushroom body has little teeth that the spores are released from.",
        "taste": "Tastes like seafood",
        "color": "White",
        "location": "Often found on beech trees",
        "inner": "White",
        "description": "The lion's mane mushroom is a species known by a variety of names. Lion’s mane mushrooms are native to the mountains of northeast Asia and may also be found in Europe and North America.",
    },

}

quiz = {
    "1": {
        "id": "1",
        "mushroom_id": "0",
        "img_url": 'images/morel_1.jpeg',
        "cut_img_url": "images/morel_open_1.png",
        "done": False
    },
    "2": {
        "id": "2",
        "mushroom_id": "1",
        "img_url": 'images/false_morel_1.jpeg',
        "cut_img_url": "images/false_morel_open_1.jpeg",
        "done": False
    },
    "3": {
        "id": "3",
        "mushroom_id": "3",
        "img_url": 'images/puffball_mushroom_1.png',
        "cut_img_url": "images/puffball_mushroom_open_1.png",
        "done": False
    },
    "4": {
        "id": "4",
        "mushroom_id": "2",
        "img_url": 'images/destroying_angel_1.jpeg',
        "cut_img_url": "images/destroying_angel_open_1.jpeg",
        "done": False
    },
    "5": {
        "id": "5",
        "mushroom_id": "4",
        "img_url": 'images/chanterelle_1.jpeg',
        "cut_img_url": "images/death_cap_1.png",
        "done": False
    },
    "6": {
        "id": "6",
        "mushroom_id": "6",
        "img_url": 'images/maitake_1.jpeg',
        "cut_img_url": "images/maitake_open_1.png",
        "done": False
    },
    "7": {
        "id": "7",
        "mushroom_id": "2",
        "img_url": 'images/destroying_angel_2.jpeg',
        "cut_img_url": "images/destroying_angel_open_2.jpeg",
        "done": False
    },
    "8": {
        "id": "8",
        "mushroom_id": "5",
        "img_url": 'images/jack_o_lantern_1.jpeg',
        "cut_img_url": "images/jack_o_lantern_open_1.jpeg",
        "done": False
    },
    "9": {
        "id": "9",
        "mushroom_id": "8",
        "img_url": 'images/lions_mane_1.jpeg',
        "cut_img_url": "images/lions_mane_open_1.jpeg",
        "done": False
    },
    "10": {
        "id": "10",
        "mushroom_id": "7",
        "img_url": 'images/oyster_1.jpeg',
        "cut_img_url": "images/oyster_1.jpeg",
        "done": False
    },
    "11": {
        "id": "11",
        "mushroom_id": "0",
        "img_url": 'images/morel_2.jpeg',
        "cut_img_url": "images/morel_open_2.jpeg",
        "done": False
    },
    "12": {
        "id": "12",
        "mushroom_id": "3",
        "img_url": 'images/puffball_2.jpeg',
        "cut_img_url": "images/puffball_open_2.jpeg",
        "done": False
    }
}


#lessons
lessons = [
    {
        "lesson_id": "1",
        "lesson_name": "True Morel",
        "mushroom1": "0",
        "img_url": 'https://media.istockphoto.com/vectors/hand-drawn-colorful-morel-mushroom-vector-id1181276056?k=6&m=1181276056&s=612x612&w=0&h=_qqA5l8WiwQpR2mRJc0mnndmzgyky-EZs_nTwl21T0U=',
        "type": "indiv",
    },
    {
        "lesson_id": "2",
        "lesson_name": "Chanterelle",
        "mushroom1": "4",
        "img_url": "/static/images/chanterelle.png",
        "type": "indiv"
    },
    {
        "lesson_id": "3",
        "lesson_name": "Puff Ball",
        "mushroom1": "3",
        "img_url": '/static/images/giantpuffball.png',
        "type": "indiv",
    },
    {
        "lesson_id": "4",
        "lesson_name": "Maitake Mushroom",
        "mushroom1": "6",
        "img_url": '/static/images/maitake.png',
        "type": "indiv",
    },
    {
        "lesson_id": "5",
        "lesson_name": "Oyster Mushroom",
        "mushroom1": "7",
        "img_url": '/static/images/oystermushroom.png',
        "type": "indiv"
    },
    {
        "lesson_id": "6",
        "lesson_name": "Lion's Mane",
        "mushroom1": "8",
        "img_url": '/static/images/lionsmane.png',
        "type": "indiv"
    },
    {
        "lesson_id": "7",
        "lesson_name": "False Morel",
        "mushroom1": "1",
        "img_url": 'https://as1.ftcdn.net/v2/jpg/02/94/34/30/1000_F_294343087_4w1GR3vVswC4RoOslk9VxORUxiRb20Rw.jpg',
        "type": "indiv",
    },
    {
        "lesson_id": "8",
        "lesson_name": "Jack o Lantern",
        "mushroom1": "5",
        "img_url": "https://healing-mushrooms.net/wp-content/uploads/2020/01/Jack-o-Lantern-Mushroom.jpg",
        "type": "indiv",
    },
    {
        "lesson_id": "9",
        "lesson_name": "Destroying Angel",
        "mushroom1": "2",
       "img_url": 'https://media.illustrationx.com/images/artist/LizPepperell/128015/watermark/1300/destroying-angel-toadstool.jpg',
        "type": "indiv",
    },
]


START_DIALOGUE = """Welcome to the wild, wild wilderness. Here we'll test everything you've learned.\n\n
                    Eat the edible mushrooms and stay away from the toxic ones!"""

ON_CHOICE_DIALOGUE = "Hmm, this looks interesting. What will you do?"

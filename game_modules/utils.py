lifes = 3
score = 0
inv_bricks = 0

colors = {
    "red": 7,
    "orange": 5,
    "green": 3,
    "yellow": 1
}


def update_score(color):
    global score
    score += colors[color]

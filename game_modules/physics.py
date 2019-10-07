from math import cos, radians, sin

from game_modules import sounds, utils

base_speed = 0.6


def calculate_angle(ball, degrees):
    dx = base_speed * cos(radians(degrees))
    dy = base_speed * sin(radians(degrees))
    ball.dx = round(dx, 2)
    ball.dy = round(dy, 2)


def collision(paddle, ball):
    brx, bry = paddle.xcor(), paddle.ycor()
    bx, by = ball.xcor(), ball.ycor()
    if (bx > brx - 60 and bx < brx + 60 and
            by - 10 <= bry + 8 and by - 10 >= bry):
        ball.sety(bry + 8 + 10)
        sounds.play_bounce()
        degrees = brx - bx + 90
        calculate_angle(ball, degrees)
    if by < bry + 8 and by > bry - 8:
        if (bx >= brx - 60 and bx < brx) or (bx <= brx + 60 and bx > brx):
            # impedir a bola de entrar na barra
            ball.sety(bry + 8 + 10)
            if (bx > brx):
                ball.setx(brx + 60)
            else:
                ball.setx(brx - 60)
            sounds.play_bounce()
            ball.dx = round(base_speed * cos(radians(30)), 2)
            # condicoes para a bola mudar de direcao em x
            if bx > brx and ball.dx <= 0:
                ball.dx *= -1
            elif bx < brx and ball.dx >= 0:
                ball.dx *= -1
            ball.dy *= -1


def collision_brick(brick, ball):
    brx, bry = brick.xcor(), brick.ycor()
    bx, by = ball.xcor(), ball.ycor()
    if brick.isvisible():
        if bx > brx - 40 and bx < brx + 40:
            if ((by - 10 <= bry + 10 and by > bry) or
                    (by + 10 >= bry - 10 and by < bry)):
                sounds.play_bounce()
                ball.dy *= -1
                utils.update_score(brick.color()[0])
                brick.hideturtle()
                return True
        if by < bry + 10 and by > bry - 10:
            if (bx >= brx - 40 and bx < brx) or (bx <= brx + 40 and bx > brx):
                ball.dx *= -1
                ball.dy *= -1
                sounds.play_bounce()
                utils.update_score(brick.color()[0])
                brick.hideturtle()
                return True
    return False

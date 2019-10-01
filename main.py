from math import cos, radians, sin
from random import randint
from time import sleep
import turtle
import os

base_speed = 0.6
ball_initial_position_x = 0
ball_initial_position_y = -220

playing = True
is_rolling = True
bricks = []
colors = {"red": 7, "orange": 5, "green": 3, "yellow": 1}

lifes = 3
score = 0
inv_bricks = 0

def create_screen(title, width, height):
    screen = turtle.Screen()
    screen.title(title)
    screen.bgcolor("black")
    screen.setup(width=width, height=height)
    screen.tracer(0)
    return screen


def close_screen():
    global playing
    playing = not playing


def create_paddle(x, y, width, length, color):
    paddle = turtle.Turtle()
    paddle.speed(0)
    paddle.shape("square")
    paddle.color(color)
    paddle.shapesize(stretch_wid=width, stretch_len=length)
    paddle.penup()
    paddle.goto(x, y)
    return paddle


def create_ball(x, y, color):
    ball = turtle.Turtle()
    ball.shape("square")
    ball.color(color)
    ball.penup()
    ball.goto(x, y)
    return ball


def create_brick(x, y, width, length, color):
    brick = turtle.Turtle()
    brick.speed(0)
    brick.shape("square")
    brick.shapesize(stretch_wid=width, stretch_len=length)
    brick.color(color)
    brick.penup()
    brick.goto(x, y)
    return brick


def create_line_of_bricks(initial_y, color):
    x = -270
    while x <= 270:
        bricks.append(create_brick(x, initial_y, 1, 4, color))
        x += 90


def create_hud(x, y):
    hud = turtle.Turtle()
    hud.speed(0)
    hud.shape("square")
    hud.color("white")
    hud.penup()
    hud.hideturtle()
    hud.goto(x, y)
    return hud


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
        os.system("aplay bounce.wav&")
        degrees = brx - bx + 90
        calculate_angle(ball, degrees)
    if by < bry + 8 and by > bry - 8:
        if (bx >= brx - 60 and bx < brx) or (bx <= brx + 60 and bx > brx):
            os.system("aplay bounce.wav&")
            ball.dx *= -1
            ball.dy *= -1


def collision_brick(brick, ball):
    global score
    global inv_bricks
    brx, bry = brick.xcor(), brick.ycor()
    bx, by = ball.xcor(), ball.ycor()
    if brick.isvisible():
        if bx > brx - 40 and bx < brx + 40:
            if ((by - 10 <= bry + 10 and by > bry) or
                    (by + 10 >= bry - 10 and by < bry)):
                os.system("aplay bounce.wav&")
                ball.dy *= -1
                score += colors[brick.color()[0]]
                update_hud()
                brick.hideturtle()
                inv_bricks += 1
                return
        if by < bry + 10 and by > bry - 10:
            if (bx >= brx - 40 and bx < brx) or (bx <= brx + 40 and bx > brx):
                ball.dx *= -1
                ball.dy *= -1
                score += colors[brick.color()[0]]
                update_hud()
                brick.hideturtle()
                inv_bricks += 1
                return


def paddle_left():   # movimentação da raquete para o lado esquerdo
    x = paddle.xcor()
    if x > -350:
        x += -40
    else:
        x = -350
    paddle.setx(x)


    if is_rolling:
        ball.setx(ball.xcor() - 40)


def paddle_right():  # movimentação da raquete para o lado direito
    x = paddle.xcor()
    if x < 340:
        x += 40
    else:
        x = 340
    paddle.setx(x)
    if is_rolling:
        ball.setx(ball.xcor() + 40)

def throw_ball():
    global is_rolling
    if is_rolling:
        px = paddle.xcor()
        bx = ball.xcor()
        degrees = px - bx + 90
        calculate_angle(ball, degrees)
        is_rolling = False


screen = create_screen("Breakout", 800, 600)
root = screen.getcanvas().winfo_toplevel()
root.protocol("WM_DELETE_WINDOW", close_screen)

# desenhando os blocos
y = 200
for color in colors.keys():
    create_line_of_bricks(y, color)
    y -= 30

paddle = create_paddle(0, -250, 0.8, 6, "white")
ball = create_ball(ball_initial_position_x, ball_initial_position_y, "white")

# definindo a velocidade inicial da bola e
# um pouco de aleatoriedade no início do jogo
if randint(0, 1) == 0:
    ball.dx = base_speed
else:
    ball.dx = -base_speed

# o jogo inicia com a bola indo pra baixo
ball.dy = 0

# movimentação da raquete
screen.listen()
screen.onkeypress(paddle_right, "Right")
screen.onkeypress(paddle_left, "Left")
screen.onkeypress(throw_ball, "space")


# mensagem de game over
def end_game_screen(string):
    hud = turtle.Turtle()
    hud.speed(0)
    hud.shape("square")
    hud.color("white")
    hud.penup()
    hud.hideturtle()
    hud.goto(0, 0)
    hud.write(string, align="center",
              font=("Press Start 2P", 24, "normal"))


score_hud = create_hud(-300, 250)
lifes_hud = create_hud(300, 250)


def update_hud():
    score_hud.clear()
    score_hud.write("SCORE {}".format(score), align="center",
                    font=("Press Start 2P", 18, "normal"))
    lifes_hud.clear()
    # tamanho e formato do coração
    lifes_hud.write("\u2764" * lifes, align="center",
                    font=("Press Start 2P",24 , "normal"))


update_hud()
while playing:
    # condição de parada do jogo
    if lifes == 0:
        update_hud()
        end_game_screen("GAME OVER :(")
        sleep(5)
        playing = False
        continue

    if inv_bricks == 28:
        update_hud()
        end_game_screen("YOU WIN :)")
        sleep(5)
        playing = False
        continue

    # movimentação da bola
    if is_rolling:
        ball.setx(ball.xcor() + ball.dx) 
        if ball.xcor() + 10 >= paddle.xcor() + 60 or ball.xcor() - 10 <= paddle.xcor() - 60:
            ball.dx *= -1
    else:
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

    collision(paddle, ball)

    for brick in bricks:
        collision_brick(brick, ball)

    # colisão com parede da direita
    if ball.xcor() > 385:
        os.system("aplay bounce.wav&")
        ball.setx(385)
        ball.dx *= -1

    # colisão com parede da esquerda
    if ball.xcor() < -388:
        os.system("aplay bounce.wav&")
        ball.setx(-388)
        ball.dx *= -1

    # colisão com parede superior
    if ball.ycor() > 288:
        os.system("aplay bounce.wav&")
        ball.dy *= -1

    # reinício do jogo - resetar a bola
    if ball.ycor() < -300:
        lifes -= 1
        update_hud()
        ball.goto(paddle.xcor(), ball_initial_position_y)
        ball.dx = base_speed
        ball.dy = 0
        is_rolling = True
        # um pouco de aleatoriedade no reinício do jogo
        if randint(0, 1) == 0:
            ball.dx *= -1

    screen.update()

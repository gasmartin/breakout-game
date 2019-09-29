from math import cos, radians, sin
from random import choice, randint
import turtle

playing = True
bricks = []
colors = ["red", "orange", "green", "yellow"]

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
    ball.speed(0)
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


# Lógica do ângulo
# px - bx + 90
def calculate_angle(ball, degrees):
    dx = ball.speed * cos(radians(degrees))
    dy = ball.speed * sin(radians(degrees))
    ball.dx = round(dx, 2)
    ball.dy = round(dy, 2)


def collision(paddle, ball):
    px, py = paddle.xcor(), paddle.ycor()
    bx, by = ball.xcor(), ball.ycor()
    if bx > px - 60 and bx < px + 60 and by - 10 <= py + 8 and by - 10 >= py:
        degrees = px - bx + 90
        calculate_angle(ball, degrees)
    if by < py + 8 and by > py - 8:
        if (bx >= px - 60 and bx < px) or (bx <= px + 60 and bx > px):
            ball.dx *= -1
            ball.dy *= -1


def paddle_left():   # movimentação da raquete para o lado esquerdo
    x = paddle.xcor()
    if x > -350:
        x += -20
    else:
        x = -350
    paddle.setx(x)


def paddle_right():  # movimentação da raquete para o lado direito
    x = paddle.xcor()
    if x < 350:
        x += 20
    else:
        x = 350
    paddle.setx(x)

screen = create_screen("Breakout", 800, 1000)
root = screen.getcanvas().winfo_toplevel()
root.protocol("WM_DELETE_WINDOW", close_screen)

paddle = create_paddle(0, -400, 0.8, 6, "white")

# posição inicial da bola
ball_initial_position_x = 0
ball_initial_position_y = 0
ball = create_ball(ball_initial_position_x, ball_initial_position_y, "white")

# definindo a velocidade inicial da bola e
# um pouco de aleatoriedade no início do jogo
if randint(0, 1) == 0:
    ball.dx = 0.7
else:
    ball.dx = -0.7

# o jogo inicia com a bola indo pra baixo
ball.dy = -0.7

# desenhando os blocos
y = 380
for color in colors:
    create_line_of_bricks(y, color)
    y -= 30
    create_line_of_bricks(y, color)
    y -= 30

# movimentação da raquete
screen.listen()
screen.onkeypress(paddle_right, "Right")
screen.onkeypress(paddle_left, "Left")

while playing:
    # movimentação da bola
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    collision(paddle, ball)

    # colisão com parede da direita
    if ball.xcor() > 385:
        ball.setx(385)
        ball.dx *= -1

    # colisão com parede da esquerda
    if ball.xcor() < -388:
        ball.setx(-388)
        ball.dx *= -1

    # colisão com parede superior
    if ball.ycor() + 10 > 500:
        ball.dy *= -1

    # reinício do jogo - resetar a bola
    if ball.ycor() < -500:
        ball.goto(paddle.xcor(), ball_initial_position_y)
        # um pouco de aleatoriedade no reinício do jogo
        if randint(0, 1) == 0:
            ball.dx *= -1

    screen.update()

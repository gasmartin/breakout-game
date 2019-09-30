from math import cos, radians, sin
from random import choice, randint
import turtle
import os

base_speed = 0.7
ball_initial_position_x = 0
ball_initial_position_y = 80
playing = True
bricks = []
colors = ["red", "orange", "green", "yellow"]
lives = 3


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
    # ball.base_speed(0)
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
    dx = base_speed * cos(radians(degrees))
    dy = base_speed * sin(radians(degrees))
    ball.dx = round(dx, 2)
    ball.dy = round(dy, 2)


def collision(paddle, ball):
    px, py = paddle.xcor(), paddle.ycor()
    bx, by = ball.xcor(), ball.ycor()
    if bx > px - 60 and bx < px + 60 and by - 10 <= py + 8 and by - 10 >= py:
        os.system("aplay bounce.wav&")
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

screen = create_screen("Breakout", 800, 600)
root = screen.getcanvas().winfo_toplevel()
root.protocol("WM_DELETE_WINDOW", close_screen)

# desenhando os blocos
y = 200
for color in colors:
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
ball.dy = -base_speed

# movimentação da raquete
screen.listen()
screen.onkeypress(paddle_right, "Right")
screen.onkeypress(paddle_left, "Left")

while playing:
    # condição de parada do jogo
    if(lives ==0):
        playing = False
        continue
    # movimentação da bola
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    collision(paddle, ball)

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
    if ball.ycor() < -450:
        lives -= 1
        os.system("aplay arcade-bleep-sound.wav&")
        ball.goto(paddle.xcor(), ball_initial_position_y)
        # um pouco de aleatoriedade no reinício do jogo
        if randint(0, 1) == 0:
            ball.dx *= -1

    screen.update()
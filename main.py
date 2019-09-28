from math import cos, radians, sin
from random import choice
import turtle

playing = True
colors = ["red", "yellow", "orange"]

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
    if bx > px - 50 and bx < px + 50 and by - 10 <= py + 8 and by - 10 >= py:
        print("Colidiu")

screen = create_screen("Breakout", 800, 600)
root = screen.getcanvas().winfo_toplevel()
root.protocol("WM_DELETE_WINDOW", close_screen)

paddle = create_paddle(0, -250, 0.8, 5, "white")
ball = create_ball(0, -150, "white")

#definindo a velocidade inicial da bola
ball.dx = 0.7
ball.dy = 0.7

bricks = []
x = -270
while x <= 270:
    y = 230
    while y >= 140:
        bricks.append(create_brick(x, y, 1, 4, choice(colors)))
        y -= 30
    x += 90

while playing:
    screen.update()

    # movimentação da bola
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
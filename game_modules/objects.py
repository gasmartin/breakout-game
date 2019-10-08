import turtle
bricks = []


def create_screen(title, width, height):
    screen = turtle.Screen()
    screen.title(title)
    screen.bgcolor("black")
    screen.setup(width=width, height=height)
    screen.tracer(0)
    return screen


def create_paddle(x, y, width, length, color):
    paddle = turtle.Turtle()
    paddle.speed(0)
    paddle.shape("square")
    paddle.color(color)
    paddle.shapesize(stretch_wid=width, stretch_len=length)
    paddle.penup()
    paddle.goto(x, y)
    return paddle


def shrink_paddle(paddle, width, new_length):
    paddle.shapesize(stretch_wid=width, stretch_len=new_length)
    paddle.goto(paddle.xcor(), paddle.ycor())


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


def create_hud(x, y):
    hud = turtle.Turtle()
    hud.speed(0)
    hud.shape("square")
    hud.color("white")
    hud.penup()
    hud.hideturtle()
    hud.goto(x, y)
    return hud


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


def create_line_of_bricks(initial_y, color):
    x = -270
    while x <= 270:
        bricks.append(create_brick(x, initial_y, 1, 4, color))
        x += 90

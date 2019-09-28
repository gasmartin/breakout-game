import turtle

playing = True

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
    brick.visible = True
    return brick

screen = create_screen("Breakout", 800, 600)
root = screen.getcanvas().winfo_toplevel()
root.protocol("WM_DELETE_WINDOW", close_screen)

paddle = create_paddle(0, -250, 1, 5, "white")
ball = create_ball(0, -25, "white")

brick = create_brick(-325, 275, 1, 5, "blue")

while playing:
    screen.update()

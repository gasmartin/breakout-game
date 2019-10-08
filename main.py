from random import randint
from time import sleep
import turtle

from game_modules import physics, sounds, utils, objects

ball_initial_position_x = 0
ball_initial_position_y = -220

playing = True
is_rolling = True
pause = False
shrink = False


def close_screen():
    global playing
    playing = not playing


screen = objects.create_screen("Breakout", 800, 600)
root = screen.getcanvas().winfo_toplevel()
root.protocol("WM_DELETE_WINDOW", close_screen)

# desenhando os blocos
y = 200
for color in utils.colors.keys():
    objects.create_line_of_bricks(y, color)
    y -= 30

paddle = objects.create_paddle(0, -250, 0.8, 6, "blue")
ball = objects.create_ball(ball_initial_position_x,
                           ball_initial_position_y, "white")

# definindo a velocidade inicial da bola e
# um pouco de aleatoriedade no início do jogo
if randint(0, 1) == 0:
    ball.dx = physics.base_speed
else:
    ball.dx = -physics.base_speed


ball.dy = 0


def paddle_left():   # movimentação da raquete para o lado esquerdo
    global pause
    global shrink
    if not pause:
        x = paddle.xcor()
        if shrink is False:
            if x > -350:
                x += -30
            else:
                x = -350
            paddle.setx(x)
        else:
            if x > -355:
                x += -30
            else:
                x = -373
            paddle.setx(x)

        if is_rolling:
            ball.setx(ball.xcor() - 30)


def paddle_right():  # movimentação da raquete para o lado direito
    global pause
    global shrink
    if not pause:
        x = paddle.xcor()
        if shrink is False:
            if x < 340:
                x += 30
            else:
                x = 340
            paddle.setx(x)
        else:
            if x < 345:
                x += 30
            else:
                x = 367
            paddle.setx(x)
        if is_rolling:
            ball.setx(ball.xcor() + 30)


def throw_ball():
    global is_rolling
    if is_rolling:
        px = paddle.xcor()
        bx = ball.xcor()
        degrees = px - bx + 90
        physics.calculate_angle(ball, degrees)
        is_rolling = False


def pause_game():
    global pause
    pause = not pause


# movimentação da raquete
screen.listen()
screen.onkeypress(paddle_right, "Right")
screen.onkeypress(paddle_left, "Left")
screen.onkeypress(throw_ball, "space")
screen.onkeypress(pause_game, "p")


score_hud = objects.create_hud(-250, 250)
lifes_hud = objects.create_hud(300, 250)
lifes_hud.color("red")


def update_hud():
    score_hud.clear()
    score_hud.write("SCORE {}".format(utils.score), align="center",
                    font=("Press Start 2P", 18, "normal"))
    lifes_hud.clear()
    # tamanho e formato do coração
    lifes_hud.write("\u2764" * utils.lifes, align="center",
                    font=("Press Start 2P", 24, "normal"))


update_hud()


while playing:

    # condição de parada do jogo
    if utils.lifes == 0:
        update_hud()
        objects.end_game_screen("GAME OVER :(")
        sounds.play_defeat()
        sleep(4)
        playing = False
        continue

    if utils.inv_bricks == 28:
        update_hud()
        objects.end_game_screen("YOU WIN :)")
        sounds.play_victory()
        sleep(4)
        playing = False
        continue

    # movimentação da bola
    if not pause:
        if is_rolling:
            ball.setx(ball.xcor() + ball.dx)

            if ball.xcor() + 10 >= paddle.xcor() + 60 or \
                    ball.xcor() - 10 <= paddle.xcor() - 60:

                ball.dx *= -1
        else:
            ball.setx(ball.xcor() + ball.dx)
            ball.sety(ball.ycor() + ball.dy)
    if utils.score < 100:
        physics.collision(paddle, ball)
    if utils.score >= 100:
        # garante que o paddle diminui apenas uma vez
        if shrink is False:
            objects.shrink_paddle(paddle, 0.8, 3)
            shrink = True
        physics.collision_shrink_paddle(paddle, ball)

    for brick in objects.bricks:
        if physics.collision_brick(brick, ball):
            utils.inv_bricks += 1
            update_hud()

    # colisão com parede da direita
    if ball.xcor() > 385:
        sounds.play_bounce()
        ball.setx(385)
        ball.dx *= -1

    # colisão com parede da esquerda
    if ball.xcor() < -388:
        sounds.play_bounce()
        ball.setx(-388)
        ball.dx *= -1

    # colisão com parede superior
    if ball.ycor() > 288:
        sounds.play_bounce()
        ball.dy *= -1

    # reinício do jogo - resetar a bola
    if ball.ycor() < -300:
        utils.lifes -= 1
        update_hud()
        ball.goto(paddle.xcor(), ball_initial_position_y)
        ball.dx = physics.base_speed
        ball.dy = 0
        is_rolling = True
        # um pouco de aleatoriedade no reinício do jogo
        if randint(0, 1) == 0:
            ball.dx *= -1

    screen.update()

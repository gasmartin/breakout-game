# criar tela
from game_modules import objects
import turtle
from time import sleep
from game_modules import objects, sounds
screen = objects.create_screen("Breakout", 800, 600)

title_hud = objects.create_hud(0, 250)
title_hud.write("BREAKOUT", align="center", font=("", 24, "normal"))

play_hud = objects.create_hud(0, 70)
play_hud.write("play", align="center", font=("", 18, "normal"))

scores_hud = objects.create_hud(0, 30)
scores_hud.write("scores", align="center", font=("", 18, "normal"))

credits_hud = objects.create_hud(0, -10)
credits_hud.write("credits", align="center", font=("", 18, "normal"))

exit_position_x = 0
exit_position_y = -50
exit_hud = objects.create_hud(exit_position_x, exit_position_y)
exit_hud.write("exit", align="center", font=("", 18, "normal"))

dx = 40
dy = 40

# para finalizar o jogo
def exit_(x, y):
    if(exit_position_x - dx <= x <= exit_position_x + dx and exit_position_y - dy <= y <= exit_position_y + dy):
        screen.bye()

screen.onscreenclick(exit_)

while True:
    screen.update()

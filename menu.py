# criar tela
from game_modules import objects
screen = objects.create_screen("Breakout", 800, 600)

title_hud = objects.create_hud(0, 250)
title_hud.write("BREAKOUT", align="center", font=("", 24, "normal"))

play_hud = objects.create_hud(0, 70)
play_hud.write("play", align="center", font=("", 18, "normal"))

scores_hud = objects.create_hud(0, 30)
scores_hud.write("scores", align="center", font=("", 18, "normal"))

credits_hud = objects.create_hud(0, -10)
credits_hud.write("credits", align="center", font=("", 18, "normal"))

exit_hud = objects.create_hud(5, -50)
exit_hud.write("exit", align="center", font=("", 18, "normal"))

while True:
    pass

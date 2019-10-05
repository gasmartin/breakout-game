# criar tela
from game_modules import objects
screen = objects.create_screen("Breakout", 800, 600)
hud_title = objects.create_hud(0, 250)
hud_title.write("BREAKOUT", align="center", font=("", 24, "normal"))
while True:
    pass

# Som de vitória - https://freesound.org/people/rezyma/sounds/475148/
# Som de derrota - https://freesound.org/people/Leszek_Szary/sounds/171673/
from os import system

def play_bounce():
    system("aplay sounds/bounce.wav&")


def play_victory():
    system("aplay sounds/victory.wav")


def play_defeat():
    system("aplay sounds/defeat.wav")

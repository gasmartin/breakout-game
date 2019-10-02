from os import system


def play_bounce():
    system("aplay sounds/bounce.wav&")


def play_victory():
    system("aplay sounds/victory.wav")


def play_defeat():
    system("aplay sounds/defeat.wav")

#Kortare mer begriplig def för klasser och funktioner, mer smooth också

from tkinter import Tk, Canvas
from classer import NormalDuck, SubaruDuck
import random
import time

path_normal_duck = "C:\\Users\\Player 1\\Documents\\Prog2\\Prog2-Annet-Nakintu-\\gränssnitt\\normalduck.png"
path_subaru_duck = "C:\\Users\\Player 1\\Documents\\Prog2\\Prog2-Annet-Nakintu-\\gränssnitt\\subduck.png"


window = Tk()

WIDTH = 600
HEIGHT = 400

canvas  = Canvas(window, width= WIDTH, height= HEIGHT )
canvas.pack()

ducks = []  # List to hold all ducks

def create_ducks(num_ducks):
    global ducks
    max_ducks = 5

    for _ in range(num_ducks):
        total_ducks = len(ducks)
        if total_ducks < max_ducks:
            duck_type = random.choice([NormalDuck, SubaruDuck])
            if duck_type == NormalDuck:
                duck = NormalDuck(canvas, random.randint(0, WIDTH), random.randint(0, HEIGHT), random.randint(1, 7), random.randint(1, 7), path_normal_duck)
            else:
                duck = SubaruDuck(canvas, random.randint(0, WIDTH), random.randint(0, HEIGHT), random.randint(8, 12), random.randint(8, 12), path_subaru_duck)
            ducks.append(duck)


# Initial creation of ducks
create_ducks(5)


while True:
    for duck in ducks:
        duck.move()
        window.update()
        time.sleep(0.01)
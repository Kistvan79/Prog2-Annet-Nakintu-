from classtest import *
import time


window = Tk()

canvas = Canvas(window, width=600, height=400)
canvas.pack()


volleyball = Ball(canvas, 0,0,1,1)

while True:
    volleyball.move()
    window.update()
    time.sleep(0.01)

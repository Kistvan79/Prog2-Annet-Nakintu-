from tkinter import *

root = Tk()
root.geometry("500x500")

canvas_width = 500
canvas_height = 500

rect_width = 10  
rect_height = 10 


center_x = canvas_width / 2
center_y = canvas_height / 2


x = center_x - (rect_width / 2)
y = center_y - (rect_height / 2)

mycanvas = Canvas(root, width=canvas_width, height=canvas_height)
mycanvas.pack(pady=20)

myrec = mycanvas.create_rectangle(x, y, x + rect_width, y + rect_height, fill="red")

def right():
    global x, move_horizontal
    if x <= 200:
        x += 10
        mycanvas.move(myrec, 10, 0)
        root.after(100,right)
    else:
        move_horizontal = "left"
        left()

def left():
    global x, move_horizontal
    if x >= 0 and move_horizontal == "left":
        x -= 10
        mycanvas.move(myrec, -10, 0)
        root.after(100, left)
    else:
        move_horizontal = "right"
        right()


def down():
    global y, move_vertical
    if y <= 200:
        y += 10
        mycanvas.move(myrec, 0, 10)
        root.after(100, down)
    else:
        move_vertical = "up"
        up()

def up():
    global y, move_vertical
    if y >= 0 and move_vertical == "up":
        y -= 10
        mycanvas.move(myrec, 0, -10)
        root.after(100, up)
    else:
        move_vertical = "down"
        down()


class Duckgo:
    pass



down()
right()
root.mainloop()
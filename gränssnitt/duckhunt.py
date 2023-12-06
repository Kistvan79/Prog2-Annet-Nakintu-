# #Duck hunt game
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.geometry("500x500")

x = 0
y = 0

mycanvas = Canvas(root, width=300, height=300, bg="white")
mycanvas.pack(pady=20)

# Paths
path = "C:\\Users\\Elev\\Documents\\Programmering2\\Prog2[Annet Nakintu]\\gränssnitt\\subduck.png"

#Open and Resize image
sub = Image.open(path)
resize = sub.resize((100,100), Image.Resampling.LANCZOS)
resized_sub = ImageTk.PhotoImage(resize)
subduck = mycanvas.create_image(0,0, anchor = NW, image=resized_sub)

def right():
    global x, move_horizontal
    if x <= 200:
        x += 10
        mycanvas.move(subduck, 10, 0)
        root.after(100,right)
    else:
        move_horizontal = "left"
        left()

def left():
    global x, move_horizontal
    if x >= 0 and move_horizontal == "left":
        x -= 10
        mycanvas.move(subduck, -10, 0)
        root.after(100, left)
    else:
        move_horizontal = "right"
        right()


def down():
    global y, move_vertical
    if y <= 200:
        y += 10
        mycanvas.move(subduck, 0, 10)
        root.after(100, down)
    else:
        move_vertical = "up"
        up()

def up():
    global y, move_vertical
    if y >= 0 and move_vertical == "up":
        y -= 10
        mycanvas.move(subduck, 0, -10)
        root.after(100, up)
    else:
        move_vertical = "down"
        down()
    
def on_click(event):
    global subduck
    x, y = event.x, event.y
    closest_item = mycanvas.find_closest(x, y)
    if closest_item and closest_item[0] == subduck:
        mycanvas.delete(subduck)
    else:
        print("Miss")


#Pack and call functions
down()
right()

mycanvas.tag_bind(subduck, "<Button-1>", on_click)
root.mainloop()
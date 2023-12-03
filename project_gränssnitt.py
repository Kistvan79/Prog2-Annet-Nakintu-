#Duck hunt game, aim training feel.
#För varje level är fåglarna snabbare


import tkinter as tk
  
class MoveCanvas(tk.Canvas):
 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
 
        self.dx = 0
        self.dy = 0
  
        self.box = self.create_rectangle(0, 0, 10, 10, fill="black")
 
        self.dt = 25
        self.tick()
      
    def tick(self):
 
        self.move(self.box, self.dx, self.dy)
        self.after(self.dt, self.tick)
 
    def change_heading(self, dx, dy):
        self.dx = dx
        self.dy = dy
  
 
if __name__ == "__main__":
 
    root = tk.Tk()
    root.geometry("300x300")
 
    cvs = MoveCanvas(root)
    cvs.pack(fill="both", expand=True)
 
    ds = 3
  
    root.bind("<KeyPress-Left>", lambda _: cvs.change_heading(-ds, 0))
    root.bind("<KeyPress-Right>", lambda _: cvs.change_heading(ds, 0))
    root.bind("<KeyPress-Up>", lambda _: cvs.change_heading(0, -ds))
    root.bind("<KeyPress-Down>", lambda _: cvs.change_heading(0, ds))
      
    root.mainloop()

#Update

# from tkinter import *

# root = Tk()
# root.geometry("500x500")

# canvas_width = 500
# canvas_height = 500

# rect_width = 10  
# rect_height = 10 


# center_x = canvas_width / 2
# center_y = canvas_height / 2


# x = center_x - (rect_width / 2)
# y = center_y - (rect_height / 2)

# mycanvas = Canvas(root, width=canvas_width, height=canvas_height)
# mycanvas.pack(pady=20)

# myrec = mycanvas.create_rectangle(x, y, x + rect_width, y + rect_height, fill="red")

# def right():
#     global x, move_horizontal
#     if x <= 200:
#         x += 10
#         mycanvas.move(myrec, 10, 0)
#         root.after(100,right)
#     else:
#         move_horizontal = "left"
#         left()

# def left():
#     global x, move_horizontal
#     if x >= 0 and move_horizontal == "left":
#         x -= 10
#         mycanvas.move(myrec, -10, 0)
#         root.after(100, left)
#     else:
#         move_horizontal = "right"
#         right()


# def down():
#     global y, move_vertical
#     if y <= 200:
#         y += 10
#         mycanvas.move(myrec, 0, 10)
#         root.after(100, down)
#     else:
#         move_vertical = "up"
#         up()

# def up():
#     global y, move_vertical
#     if y >= 0 and move_vertical == "up":
#         y -= 10
#         mycanvas.move(myrec, 0, -10)
#         root.after(100, up)
#     else:
#         move_vertical = "down"
#         down()

# down()
# right()
root.mainloop()

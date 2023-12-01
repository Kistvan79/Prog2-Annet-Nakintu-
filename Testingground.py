import tkinter as tk
class Moving:
    def __init__(self, hp):
        self.hp = hp


def move_rectangleD():
    canvas.move(rectangle, 5, 0)
    window.after(100, move_rectangleD)

def move_rectangleU():
    canvas.move(rectangle,0,5)
    window.after()


    

window = tk.Tk()
window.geometry("500x500")

canvas = tk.Canvas(window, width=400, height=400, bg="white")
rectangle = canvas.create_rectangle(10, 10, 20, 20, fill="red")
canvas.pack(pady=20)

move_rectangle()

window.mainloop()

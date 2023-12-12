from tkinter import *
from PIL import ImageTk, Image

path_normal_duck = "C:\\Users\\Player 1\\Documents\\Prog2\\Prog2-Annet-Nakintu-\\gränssnitt\\subduck.png"
path_subaru_duck = "C:\\Users\\Player 1\\Documents\\Prog2\\Prog2-Annet-Nakintu-\\gränssnitt\\subduck.png"


class NormalDuck:
    
    def __init__(self, canvas, x,y, xvelocity, yvelocity):
        self.canvas = canvas
        duck = Image.open(path_normal_duck)
        resize = duck.resize((80,80), Image.Resampling.LANCZOS)
        self.resized = ImageTk.PhotoImage(resize)
        self.image = canvas.create_image(x,y, image = self.resized)
        self.xvelocity = xvelocity
        self.yvelocity = yvelocity

    def move(self):
        coordinates = self.canvas.coords(self.image)

        if (coordinates[0]>=(self.canvas.winfo_width()) or coordinates[0]<0):
            self.xvelocity = -self.xvelocity
        if (coordinates[1]>=(self.canvas.winfo_height()) or coordinates[1]<0):
            self.yvelocity = -self.yvelocity
        self.canvas.move(self.image,self.xvelocity,self.yvelocity)

class SubaruDuck(NormalDuck):
    def __init__(self, canvas, x, y, xvelocity, yvelocity):
        super().__init__(canvas, x, y, xvelocity, yvelocity)
        self.canvas = canvas
        subaru_duck = Image.open(path_subaru_duck)
        s_resize = subaru_duck.resize((80,80), Image.Resampling.LANCZOS)
        self.resized_subaru_duck = ImageTk.PhotoImage(s_resize)
        self.image = canvas.create_image(x,y, image = self.resized_subaru_duck)
        self.xvelocity = xvelocity
        self.yvelocity = yvelocity



        
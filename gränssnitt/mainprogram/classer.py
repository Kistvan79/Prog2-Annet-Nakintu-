from tkinter import *
from PIL import ImageTk, Image


class NormalDuck:
    
    def __init__(self, canvas, x,y, xvelocity, yvelocity, image_path):
        self.canvas = canvas
        duck = Image.open(image_path)
        resize = duck.resize((80,80), Image.Resampling.LANCZOS)
        self.resized = ImageTk.PhotoImage(resize)
        self.image = canvas.create_image(x,y, image = self.resized)
        self.xvelocity = xvelocity
        self.yvelocity = yvelocity
        self.canvas.tag_bind(self.image, "<Button-1>", self.on_click)

    def move(self):
        if self.image is not None:
            coordinates = self.canvas.coords(self.image)

            if coordinates:
                if (coordinates[0]>=(self.canvas.winfo_width()) or coordinates[0]<0):
                    self.xvelocity = -self.xvelocity

                if (coordinates[1]>=(self.canvas.winfo_height()) or coordinates[1]<0):
                    self.yvelocity = -self.yvelocity
                self.canvas.move(self.image,self.xvelocity,self.yvelocity)
    
    def on_click(self, event):
        x, y = event.x, event.y
        closest_item = self.canvas.find_closest(x, y)
        if closest_item and closest_item[0] == self.image:
            self.canvas.delete(self.image)
            self.image == None


class SubaruDuck(NormalDuck):
    def __init__(self, canvas, x, y, xvelocity, yvelocity, image_path):
        super().__init__(canvas, x, y, xvelocity, yvelocity, image_path)
        duck = Image.open(image_path)
        resize = duck.resize((80,80), Image.Resampling.LANCZOS)
        self.resized = ImageTk.PhotoImage(resize)
        self.image = canvas.create_image(x,y, image = self.resized)
        self.canvas.tag_bind(self.image, "<Button-1>", self.on_click)
    



        
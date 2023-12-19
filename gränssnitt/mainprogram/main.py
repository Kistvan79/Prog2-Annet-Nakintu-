#Kortare mer begriplig def för klasser och funktioner, mer smooth också

from tkinter import *
from classer import max_time
from PIL import ImageTk, Image
import threading
import random
import vlc
import time

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
    
    def quack(self):
        quack = vlc.MediaPlayer("gränssnitt\\sounds\\quacksound.mp3")
        return quack.play()
    
    def on_click(self, event):
        x, y = event.x, event.y
        closest_item = self.canvas.find_closest(x, y)
        if closest_item and closest_item[0] == self.image:
            self.quack()
            self.canvas.delete(self.image)
            ducks.remove(self)
            del self
            create_ducks()
        
class SubaruDuck(NormalDuck):
    def __init__(self, canvas, x, y, xvelocity, yvelocity, image_path):
        super().__init__(canvas, x, y, xvelocity, yvelocity, image_path)
        duck = Image.open(image_path)
        resize = duck.resize((80,80), Image.Resampling.LANCZOS)
        self.resized = ImageTk.PhotoImage(resize)
        self.image = canvas.create_image(x,y, image = self.resized)
        self.canvas.tag_bind(self.image, "<Button-1>", self.on_click)


        
PATH_NORMAL_DUCK = "gränssnitt\\photos\\normalduck.png"
PATH_SUBARU_DUCK = "gränssnitt\\photos\\subduck.png"


window = Tk()

WIDTH = 600
HEIGHT = 400

canvas = Canvas(window, width= WIDTH, height= HEIGHT, bg="skyblue")
canvas.pack()

ducks = []  # List to hold all ducks
def create_ducks():
    global ducks
    max_ducks = 5

    for _ in range(max_ducks):
        total_ducks = len(ducks)
        if total_ducks < max_ducks:
            duck_type = random.choice([NormalDuck, SubaruDuck])
            if duck_type == NormalDuck:
                duck = NormalDuck(canvas, random.randint(0, WIDTH), random.randint(0, HEIGHT), random.randint(1, 7), random.randint(1, 7), PATH_NORMAL_DUCK)
            else:
                duck = SubaruDuck(canvas, random.randint(0, WIDTH), random.randint(0, HEIGHT), random.randint(8, 12), random.randint(8, 12), PATH_SUBARU_DUCK)
            ducks.append(duck)


create_ducks()
daemon_time = threading.Thread(target=max_time, daemon=True)
daemon_time.start()


while True:
    for duck in ducks:
        duck.move()
        window.update()
        time.sleep(0.01)
# # #Duck hunt game
from tkinter import *
from PIL import ImageTk, Image
import random

class Duck:
    def __init__(self, canvas, speed):
        self.canvas = canvas
        self.speed = speed
        self.image = canvas.create_image(300,150, image = resized_sub)  # Change this to your duck image
        self.vector = self.generate_random_vector()
        self.move_duck()

        canvas.tag_bind(self.image, "<Button-1>", self.on_click)

    def generate_random_vector(self):
        return [random.uniform(-1, 1), random.uniform(-1, 1)]

    def move_duck(self):
        self.canvas.move(self.image, self.vector[0] * self.speed, self.vector[1] * self.speed)
        pos = self.canvas.coords(self.image)
        if pos[0] <= 0 or pos[0] >= self.canvas.winfo_width():
            self.vector[0] *= -1
        if pos[1] <= 0 or pos[1] >= self.canvas.winfo_height():
            self.vector[1] *= -1
        self.canvas.after(50, self.move_duck)  # Adjust the speed of the movement

    def on_click(self, event):
        x, y = event.x, event.y
        closest_item = self.canvas.find_closest(x, y)
        if closest_item and closest_item[0] == self.image:
            self.canvas.delete(self.image)
        else:
            print("Miss")


def create_ducks(canvas, num_ducks):
    ducks = []
    for _ in range(num_ducks):
        speed = random.randint(1, 3)
        duck = Duck(canvas, speed)
        ducks.append(duck)
    return ducks

# # Paths
path_to_subduck = "C:\\Users\\Elev\\Documents\\Programmering2\\Prog2[Annet Nakintu]\\gränssnitt\\subduck.png"

root =Tk()
canvas = Canvas(root, width=600, height=400, bg='sky blue')
sub = Image.open(path_to_subduck)
resize = sub.resize((80,80), Image.Resampling.LANCZOS)
resized_sub = ImageTk.PhotoImage(resize)
ducks = create_ducks(canvas, 5)  # Change the number of ducks as needed

root.title("Duck Game")
canvas.pack()
root.mainloop()

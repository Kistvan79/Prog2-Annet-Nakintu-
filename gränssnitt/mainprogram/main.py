#VLC kan behövas laddas ner innan spelet.
from tkinter import *
from PIL import ImageTk, Image
import random
import vlc


class NormalDuck:
    def __init__(self, canvas, x,y, xvelocity, yvelocity, image_path, points):
        self.canvas = canvas
        self.points = points
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
        quack = vlc.MediaPlayer("sounds\\quacksound.mp3")
        quack.play()
    
    def on_click(self, event):
        x, y = event.x, event.y
        closest_item = self.canvas.find_closest(x, y)
        if closest_item and closest_item[0] == self.image:
            update_scoreboard(self.points)
            self.quack()
            self.canvas.delete(self.image)
            ducks.remove(self)
            del self
            create_ducks()
        
class SubaruDuck(NormalDuck):
    def __init__(self, canvas, x, y, xvelocity, yvelocity, image_path, points):
        super().__init__(canvas, x, y, xvelocity, yvelocity, image_path, points)
        duck = Image.open(image_path)
        resize = duck.resize((80,80), Image.Resampling.LANCZOS)
        self.resized = ImageTk.PhotoImage(resize)
        self.image = canvas.create_image(x,y, image = self.resized)
        self.canvas.tag_bind(self.image, "<Button-1>", self.on_click)

class PufferFish(NormalDuck):
    def __init__(self, canvas, x, y, xvelocity, yvelocity, image_path, points):
        super().__init__(canvas, x, y, xvelocity, yvelocity, image_path, points)
        puffer_fish = Image.open(image_path)
        resize = puffer_fish.resize((80,80), Image.Resampling.LANCZOS)
        self.resized = ImageTk.PhotoImage(resize)
        self.image = canvas.create_image(x,y, image = self.resized)
        self.canvas.tag_bind(self.image, "<Button-1>", self.on_click)

    def quack(self):
        super().quack()
        puffer_quack = vlc.MediaPlayer("sounds\\puffersound.mp3")
        puffer_quack.play()




def create_ducks():
    global ducks
    max_ducks = 5

    for _ in range(max_ducks):
        total_ducks = len(ducks)
        if total_ducks < max_ducks:
            random_number = random.random()
            if random_number < 0.4:
                duck = NormalDuck(canvas, random.randint(0, WIDTH), random.randint(0, HEIGHT), random.randint(1, 4), random.randint(1, 3), PATH_NORMAL_DUCK, 5)
            elif random_number < 8 and random_number > 0.4:
                duck = SubaruDuck(canvas, random.randint(0, WIDTH), random.randint(0, HEIGHT), random.randint(5, 8), random.randint(3, 5), PATH_SUBARU_DUCK, 10)
            else:
                duck = PufferFish(canvas, random.randint(0, WIDTH), random.randint(0, HEIGHT), 12, 8, PATH_PUFFER_FISH, 50)
            ducks.append(duck)



def update_scoreboard(points):
    global score, running_game
    if running_game:
        score += points
        canvas.itemconfig(scoreboard, text=f"SCORE: {score}")
        canvas.tag_lower(scoreboard)
        window.after(1, update_scoreboard) # TypeError ursprung. 
    

def max_time(countdown):
    global score, game_over
    if countdown >= 0:
        seconds = countdown % 60
        minutes = countdown // 60
        canvas.delete("timer")  # Clear previous text
        timer_text = canvas.create_text(300, 100, text=f"{minutes:02}:{seconds:02}", fill="white", font=("System", 100), tags="timer")
        canvas.tag_lower(timer_text)
        window.after(1000, max_time, countdown - 1)  # Call max_time again after 1000ms (1 second)
    else:
        game_over = True
        score = 0
        button_frame.pack()
        print("THE END!")

def start_game():
    global running_game 
    running_game.set(True)
    create_ducks()
    max_time(60)
    button_frame.pack_forget()
    update_scoreboard(-score)

def game_loop():
    if running_game:
        for duck in ducks:
            duck.move()
        window.after(10, game_loop)

def quit_game():
    window.destroy()

def intro():
    global button_frame, running_game

    running_game = BooleanVar()
    running_game.set(False)

    button_frame = Frame(window)
    button_frame.pack()

    start_button = Button(button_frame, text="Start Game", width=10, height=2, bd="5", command=start_game)
    start_button.pack(pady=10)

    quit_button = Button(button_frame, text="Quit", width=10, height=2, bd="5", command=quit_game)
    quit_button.pack(pady=10)

#Path to images, Path to dogE och vicdog är bilder som inte han göra nytta av.
PATH_NORMAL_DUCK = "photos\\normalduck.png"
PATH_SUBARU_DUCK = "photos\\subduck.png"
PATH_PUFFER_FISH = "photos\\pufferfish.png"



window = Tk()
window.title("Execute The Ducks")
WIDTH = 700
HEIGHT = 400

canvas = Canvas(window, width= WIDTH, height= HEIGHT, bg="skyblue")
canvas.pack()

scoreboard = canvas.create_text(canvas.winfo_width()+80, 20, text="", fill="white", font=("System", 25))
game_over = False
ducks = []  # List to hold all ducks
score = 0
running_game = False

intro()
game_loop()
window.mainloop()
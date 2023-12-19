import time
from main import canvas

def max_time():
    game_time = int(60*3)
    for x in range(game_time, 0, -1):
        seconds = x % 60
        minutes = int(x / 60) % 60
        canvas.create_text(300,100, text=f"{minutes:02}:{seconds:02}", fill="white")
        time.sleep(1)
    print("THE END!")



        
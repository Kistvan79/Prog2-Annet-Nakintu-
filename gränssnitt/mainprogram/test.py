from tkinter import *

window = Tk()

WIDTH = 600
HEIGHT = 400

canvas = Canvas(window, width= WIDTH, height= HEIGHT, bg="skyblue")
canvas.pack()

def max_time(countdown):
    if countdown >= 0:
        seconds = countdown % 60
        minutes = countdown // 60

        canvas.delete("timer")  # Clear previous text
        test = canvas.create_text(300, 100, text=f"{minutes:02}:{seconds:02}", fill="white", font=("Playbill", 24), tags="timer")
        canvas.tag_lower(test)
        window.after(1000, max_time, countdown - 1)  # Call max_time again after 1000ms (1 second)
    else:
        print("THE END!")

# Start the countdown timer with 3 minutes (180 seconds)
max_time(5)

window.mainloop()
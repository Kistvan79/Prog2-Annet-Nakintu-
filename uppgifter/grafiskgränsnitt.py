from tkinter import *
import random
window = Tk()
rock = Button(window, text= "rock", command=lambda: rockpaperscissors("rock"))
paper = Button(window, text= "paper", command=lambda: rockpaperscissors("paper"))
scissor = Button(window, text= "scissor", command=lambda: rockpaperscissors("scissor"))
def rockpaperscissors(user_choice):
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    lbl["text"] = "Du valde: " + user_choice
    com["text"] = "Computer valde: " + computer_choice

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        res["text"] = "It's a tie"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissor" and computer_choice == "paper")
    ):
        res["text"] = "You win!"
    else:
        res["text"] ="Computer wins!"

print("Thanks for playing!")

lbl = Label(window)
com = Label(window)
res = Label(window)

rock.pack()
scissor.pack()
paper.pack()
lbl.pack()
com.pack()
res.pack()
window.geometry("500x500")

window.mainloop()
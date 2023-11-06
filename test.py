from tkinter import *
root = Tk()
b = Button(root, text ="Tryck mig!")
def click_handler(self):
    lbl["text"] = "Du skrev: "
b.bind("<Button-1>", click_handler)
b.pack()
lbl = Label(root)
lbl.pack()
root.mainloop()


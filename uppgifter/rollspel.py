import random as rand
from tkinter import *

class Races:
    def __init__(self, ålder, kropp, attytid, ability, pickme, sty, sto, fys, smi, int, psy, kar):
        self.ålder = ålder
        self.kropp = kropp
        self.attytid = attytid
        self.ability= ability
        self.pickme = pickme
        self.sty = sty
        self.sto = sto
        self.fys = fys
        self.smi = smi
        self.int = int
        self.psy = psy
        self.kar= kar

    def livslängd(self):
        pass
    def utseende(self):
        pass
    def uppträdande(self):
        pass
    def speciellt(self):
        pass
    def förmåga(self):
        pass
    def dice(self):
        pass


class Halvalv(Races):
    def __init__(self, ålder, kropp, attytid, ability, pickme, sty, sto, fys, smi, int, psy, kar):
        super().__init__(ålder, kropp, attytid, ability, pickme, sty, sto, fys, smi, int, psy, kar)

class Hober(Races):
    def __init__(self, ålder, kropp, attytid, ability, pickme, sty, sto, fys, smi, int, psy, kar):
        super().__init__(ålder, kropp, attytid, ability, pickme, sty, sto, fys, smi, int, psy, kar)

class Människa(Races):
    def __init__(self, ålder, kropp, attytid, ability, pickme, sty, sto, fys, smi, int, psy, kar):
        super().__init__(ålder, kropp, attytid, ability, pickme, sty, sto, fys, smi, int, psy, kar)

def roll(sides, times = 1):
    score = 0
    for _ in range(times):
        score += rand.randint(1, sides)
        return score

def slumpmässigttal():
    return rand.randint(1,10)


def spelet():
    rpg = Tk()
    sty_att = Label(rpg)
    sto_att = Label(rpg)
    fys_att = Label(rpg)
    smi_att = Label(rpg)
    int_att = Label(rpg)
    psy_att = Label(rpg)
    kar_att = Label(rpg)

    rand_att = Button(rpg, text="Random points giver", command= slumpmässigttal())

    player_name = Entry(rpg)
    sty_att["text"] = f"Din styrka är : {slumpmässigttal()}"
    sto_att["text"] = f"Din stoicism är : {slumpmässigttal()}"
    fys_att["text"] = f"Din fysik är : {slumpmässigttal()}"
    smi_att["text"] = f"Din smitta är : {slumpmässigttal()}"
    int_att["text"] = f"Din intelligence är : {slumpmässigttal()}"
    psy_att["text"] = f"Din psykologi är : {slumpmässigttal()}"
    kar_att["text"] = f"Din kardio är : {slumpmässigttal()}"

    rand_att.pack()
    sty_att.pack()
    sto_att.pack()
    fys_att.pack()
    smi_att.pack()
    int_att.pack()
    psy_att.pack()
    kar_att.pack()
    player_name.pack()
    rpg.geometry("500x500")
    rpg.mainloop()
    
spelet()
    
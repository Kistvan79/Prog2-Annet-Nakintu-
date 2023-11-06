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

def spelet():
    rpg = Tk()
    player_name = Entry(rpg)
    sty_att["text"] = "Din styrka är : "
    sto_att["text"] = "Din stoicism är : "
    fys_att["text"] = "Din fysik är : "
    smi_att["text"] = "Din smitta är : "
    int_att["text"] = "Din intelligence är : "
    psy_att["text"] = "Din psykologi är : "
    kar_att["text"] = "Din kardio är : "
    player_name.pack()
    rpg.geometry("500x500")
    rpg.mainloop()
    
def roll(sides, times = 1):
    score = 0
    for _ in range(times):
        score += rand.randint(1, sides)
        return score
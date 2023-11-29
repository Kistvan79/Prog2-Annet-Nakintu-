#Attack on Djuren

class Djur:
    def __init__(self, namn, hp, styrka):
        self.nam = namn
        self.hp = hp
        self.str = styrka
    
    def attack(self):
        print("Djuret äter giftig karamel")
    
    def sov(self):
        print("Djuret sover")

class Fågel(Djur):
    def __init__(self, namn, vingspann):
        super().__init__(namn)
        self.vingspann = vingspann

class Fisk(Djur):
    def __init__(self, namn, maxdjup):
        super().__init__(namn)
        self.maxdjup = maxdjup

    def simma(self):
        print("Fisken simmar, what a legend")

class Haj(Fisk):
    def __init__(self, namn, maxdjup: int, antaltänder):
        super().__init__(namn, maxdjup)
        self.antaltänder = antaltänder
    
    def ät(self, djur: Djur):
        print("Hajen åt", djur.namn, "!")

class Torsk(Fisk):
    def __init__(self, namn, maxdjup, hastighet):
        super().__init__(namn, maxdjup)
        self.hastighet = hastighet

def fånga(torsk, haj):
        if torsk.hastighet < 30 and haj.maxdjup >= torsk.maxdjup:
            print("True")
        else:
            print("False")

haj = Haj("Robina",30, 69)
torsk = Torsk("Linnèa", 10, 29)
fånga(torsk, haj)
haj.ät(torsk)
torsk.sov()
torsk.ät()

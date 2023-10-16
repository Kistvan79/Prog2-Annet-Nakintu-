class Djur:
    def __init__(self, namn):
        self.namn = namn

class Fågel(Djur):
    def __init__(self, namn, vingspann):
        super().__init__(namn)
        self.vingspann = vingspann

class Fisk(Djur):
    def __init__(self, namn, maxdjup):
        super().__init__(namn)
        self.maxdjup = maxdjup

class Haj(Fisk):
    def __init__(self, namn, maxdjup, antaltänder):
        super().__init__(namn, maxdjup)
        self.antaltänder = antaltänder

class Torsk(Fisk):
    def __init__(self, namn, maxdjup, hastighet):
        super().__init__(namn, maxdjup)
        self.hastighet = hastighet

def fånga(torsk, haj):
        if torsk.hastighet < 30 and haj.maxdjup >= torsk.maxdjup:
            print("True")
        else:
            print("False")

robin = Haj("Robina",30, 30)
linnea = Torsk("Linnèa", 10, 29)
fånga(linnea, robin)
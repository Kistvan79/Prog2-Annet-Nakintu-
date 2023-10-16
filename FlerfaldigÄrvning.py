class Djur:
    def __init__(self, namn, kusiner):
        self.namn = namn
        self.kusiner = kusiner
    
    def dö(self):
        print(self.namn,"Har dödat sig själv")

    def äta(self):
        print(self.namn, "Äter frasiga kex")


class Däggdjur(Djur):
    def __init__(self, ångest, namn, kusiner):
        super().__init__(namn, kusiner)
        self.ångest = ångest
    
    def prata(self):
        print(self.namn, "Snackar om fantastiska uppleverlser")

class Landdjur(Djur):
    def __init__(self, hastighet, namn, kusiner):
        super().__init__(namn, kusiner)
        self.hastighet = hastighet

    def bli_jobbig(self):
        if self.hastighet > 100:
            print(self.namn, "är super jobbig, smh")
        else:
            print(self.namn, "Har det chill, inget at på peka")

class Havsdjur(Djur):
    def __init__(self, andas, namn, kusiner):
        super().__init__(namn, kusiner)
        self.andas = andas
    
    def simma(self):
        print(self.namn, "simmar utan hastighet!")

class Häst(Däggdjur, Landdjur):
    def __init__(self, hastighet, ångest, namn, kusiner):
        Däggdjur.__init__(ångest, namn, kusiner)
        Landdjur.__init__(self, hastighet)
    
    def spring(self):
        print("Spring")

class Val(Däggdjur, Havsdjur):
    def __init__(self, andas, ångest, namn, kusiner):
        super().__init__(ångest, namn, kusiner)
        Havsdjur.__init__(self, andas)
    
    def bal(self):
        print("Val på Bal")
    
class Fisk(Havsdjur):
    def __init__(self, andas, namn, kusiner):
        super().__init__(andas, namn, kusiner)

    def kpop(self):
        print(self.namn "spannar in kpop dansare för att fly!")

class Ödla(Landdjur):
    def __init__(self, hastighet, namn, kusiner):
        super().__init__(hastighet, namn, kusiner)

    def Zucker(self):
        print(self.kusiner, "Har bjudit in Zuckerburg i facebook gruppen")
        print(self.namn, "Är shockad")
        self.dö()




    
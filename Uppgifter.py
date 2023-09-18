#28 august 2023
###Rövarspråk

# user = input("")
# rövar = ""
# konsonanter = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","z"]

# for bokstav in list(user):
#     if bokstav in konsonanter:
#         rövar += bokstav+"O"+bokstav
#     else:
#         rövar += bokstav

# print(rövar)

###Andra uppgiften

# user = input("")
# reverse = user[::-1]
# print("This is reverse: "+reverse)

###Tredje uppgiften

# d = {"Sweden":"Stockholm", "Finland":"Helsinki", "Norge":"Oslo","Danmark":"Copenhagen"}
# print(d["Sweden"])
# d.update({"USA":"Washington DC"})
# d.pop("Danmark")
# print(d)

###Fjärde uppgiften

# frukt = {"Äpple", "Päron", "Banan"}
# exotiskish = {"Ananas", "Kiwi", "Päron"}

# frukt.union(exotiskish)
# print(frukt)
#I ett set, can det ej finnas 2 av samma element!

#30 august 2023 Flödesstyrning
###Uppgift 1.

# for tal in range(999):
#     if tal % 7 == 0:
#         print(tal)
#     else:
#         continue

###Uppgift 2
# while True:
    # try:
    #     user_input = input()
    #     print("This is INPUT: "+user_input)
    #     siffra = 1
    #     for siffra in user_input:
    #         print(siffra)
    #     print("Antal siffror: " + siffra)
    # except:
    #     print("Snälla mät in ett heltal")

### 4 sept 2023
##Palindrome checker
# while True:
#     user_input=input("")
#     p = user_input[::-1]
#     if p == user_input:
#         print("Yes")
#     elif p != user_input:
#         print("No")
#     else:
#         print("ERRoR")

##Password Strength checkerjgdjd
# while True:
#     user_input=input("")
#     if len(user_input) >= 8:
#         print("Password length: ",len(user_input))
#         print(f"arg 1: {any(char.isupper() for char in user_input)}")
#         print(f"arg 2: {any(char.islower() for char in user_input)}")
#     if any(char.isupper() for char in user_input) and any(char.islower() for char in user_input):
#         print("Does password have lowercase and uppercase?: True")
#     else:
#         print("")
#     if any(char.isdigit() for char in user_input):
#         print("Does password include digits?: True")
    

### 6 sept 2023
#Object-orientering.
#1
# class Elev:
    
#     def __init__(self, name, ålder):
#         self.name = name
#         self.ålder = ålder
# elev = Elev("Margareta", 23)
#2 & 3
# class Elev:
    
#     def __init__(self, name, ålder, godkänd):
#         self.name = name
#         self.ålder = ålder
#         if (godkänd == True):
#             self.glad = True

#     def presenter(self):
#         print(f"Hej jag heter {self.name}!")

# elev = Elev("Margareta", 23, True)
# elev.presenter()

# print(elev.glad)

###GPT UPPGIFT
# import datetime

# class Account:

#     def __init__(self, name, email, password):
#         self.name = name
#         self.email = email
#         self.password = password
    
#     def current_time(self):
#         self.time = datetime.datetime.now()
#         print(self.time)

#     def details_verification(self):
#         if any(char in "@" for char in email):
#             print("Cooolt")

# print("Please input your User name, Email, Password in that order")
# user_details = input("")
# name, email, password = user_details.split()
# user_account = Account(name, email, password)

# print(user_account.__dict__)
# user_account.current_time()
# user_account.details_verification()

###Uppgift clar!
# class Bil:
#     __maxHastighet = 0
#     def __init__(self, maxHastighet):
#          self.__maxHastighet = maxHastighet 
#     def setMaxhastighet(self, maxHastighet):
#             self.__maxHastighet = maxHastighet
#             return maxHastighet
                        
#     def getMaxhastighet(self):
#         return self.__maxHastighet

#     @staticmethod
#     def milestokm(miles):
#         return 1.6093*miles
    


# bil = Bil(21)

# print(bil.getMaxhastighet())
# print(bil.milestokm(31))
# print(bil.setMaxhastighet(31))

## 13 september 2023
# def add_this(*input):
#     summa = 0
#     for tal in input:
#         summa += tal
#     return summa

# print(add_this(1,2,3))
# print(add_this(1,2,3,4,5))
##Vad har jag lärt mig?: Return statements är viktiga ifall man vill få ut något.

# def food(edible, vegan=False):
#     if edible == "mjölk" and vegan == True:
#         return "sojamjölk"
#     else:
#         return edible
# print(food("mjölk"))
# print(food("mjölk", True))
## Vad har jag lärt mig?: Sojamjölk kommer aldrig att vara god.

##Inför prov

# line = input()
# a, b = line.split()
# a = int(a)
# b = int(b)
# if a > b:
#     a, b = b, a
#     print(b-a)
# else:
#     print(b-a)



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

# line = input()
# a, b = line.split(" ")
# a = int(a)
# b = int(b)

# if a < b:
#     difference = b - a
# else:
#     difference = a - b

# print(difference)

#Programmering 2 övnings uppgifter

### Uppgift 2

# def double(i): ## Är en method som intar ett värde
#     return i*2 ## Returnerar värdet gånger 2
# print(double(4)) ## Ger 8
# print(double("åtta")) ## Krashar, det går ej att använda matematiska statements med strings och integers
# print(double([1, 2])) ## Krashar, man ställer in en lista inte en variable

#stringen upprepas
#listan upprepas och värderna lägs till i den gamla listan.

### Uppgift 3

#Det går ej att dela något med noll
#Därför printas något gick fel och Nu är undan...
# x = 10
# try:
#     x/0
#     print("Allt gick bra.")
# except:
#     print("Något gick fel.")
# finally:
#     print("Nu är undantagshanteringen klar.")

### Uppgift 4

#det är en float datatyp, skriver ut medianen
# def funk(*args):
# 	return sum(args)/len(args)
# print(funk(2, 4, 6, 8))
# print(type(funk(2,4,6,8)))

### Uppgift 5

# greet("Martin") ## Hej Martin
# greet("Martin", "eng") ## Hello Martin
# greet("Martin", "fin") ##¯\_(ツ)_/
# def greet(name, lang="swe"):
#     if lang == "swe":
#         print(f"Hej {name}")
#     elif lang == "eng":
#         print(f"Hello {name}")
#     elif lang == "fr":
#         print(f"Bonjour {name}")
#     else:
#         print(f"¯\_(ツ)_/")

# greet("Martin")
# greet("Martin", "eng")
# greet("Martin", "fin")

### Uppgift 1 TBLR

## Kattis A New Alphabet not done at all

# input = input()
# newalpha = ["@","8","(","|)","3","#","6","[-]","|","_|","|<","1","[]\/[]","[]\[]","0","|D","(,)","|Z","$","']['","|_|","\/","\/\/","}{","`/","2"]
# oldalpha = "abcdefghijklmnopqrstuvwxyz"
# output = ""

# for i in input:
#     if i in oldalpha:
#         print(oldalpha[len(input)-1])

# line = input()
# split = list(map(int, line.split()))
# count = 0
# print(split[1])
# for num in split:
#     if num > split[count]: ## How in the tarnation is it out of range???
#         res = num - split[count]
#         count += 1
#     else:
#         res = split[count] - num
#         count += 1
# print(res)

## Echo Uppgift work in progress
# n = int(input())
# # shout = input()
# # splitshout = shout.split()
# count = 1
# # echo = ""
# # for string in splitshout:
# #     if n % count == 1 or 0:
# #         echo += string 
# #         echo += " "
# #         count += 1
# #     else:
# #         print("That didnt work")

# # print(echo)

# # while True:
# #     res = n- count % 2
# #     if res == 4:
# #         count += 1
# #         print(res)
# #     else:
# #         print(res)
# #         count += 1
# #     if count == 5:
# #         break

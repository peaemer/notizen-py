import math
import time
#https://www.youtube.com/watch?v=XKHEtdqhLK8  Video
#_______________________________________________________________________________________________________________________
#while loop und While not loops mehr info auf ZEILE 105
name = ""
while len(name) ==0:
    name = input("Wie ist dein Name?: ")

age = None
while not age:
    age = int(input("Wie alt bist du?: "))

height = None
while not height:
    height = float(input("Wie groß bist du?: "))

my_name = "Jack Saering"

                                                                                                                        #int
#age += 1
pi = 3.14
x = 4
y = 3
z = 2

print(round(pi))
print(math.ceil(pi))
print(abs(pi))
print(pow(pi,2))
print(math.sqrt(pi))
print(max(x,y,z))

human = False                                                                                                           #booleans

name1, age1, human1 = "Jessy", 26, True                                                                                 #multiple assigmnent
Jack = Jonas = Cora = Johanna = Tobias = "IT Klasse"

print("Hallo "+name.upper()+" wie geht es dir?")                                                                        #string Methods .method() nach nem string
print("ich bin: "+str(age)+" Jahre alt.")                                                                               #+str() um int oder andere werte zu schreiben

print("Ich bin: "+str(height)+" cm groß!")

print("Bin ich menschlich? "+str(human))

print(Jack)
print(Jonas)
print(Cora)
print(Johanna)

#_______________________________________________________________________________________________________________________

print(name*4)                                                                                                           #wie oft soll etwas displayd wer



print(float(age))
print(int(height))
print(int(len(name*4)))
#_______________________________________________________________________________________________________________________

#Slicing indexing[] slice() [start:stop:step]

first_name = my_name[0:4]
last_name = my_name[5:]
encode_name = my_name[0:12:3]
reversed_name = my_name[::-1]

print(last_name)
print(first_name)
print(encode_name)
print(reversed_name)


website = "http://google.com"
website1 = "http://Youtube.com"

slice = slice(7,-4)

print(website[slice])
print(website1[slice])

#_______________________________________________________________________________________________________________________
#if statements
#logical operator (and,or,not)

if age == 100:
    print("GZ du alter sack!")
elif age >= 18:
    print("https://pornhub.com")
elif age < 0:
    print("was bist du? Benjamin Button?")
else:
    print("Sorry nicht alt genug!:c")

temp = int(input("Wie warm ist es heute?: "))

if not(temp >= 0 and temp <= 30):
    print("übel das schlimme Wetter!")
elif not(temp < 0 or temp > 30):
    print("Temperatur geht voll klar!")
else:
    print("Scheiß wetter!")
#_______________________________________________________________________________________________________________________
#while loops: werden solange ausgeführt bis sich die Parameter ändern
#while not: siehe Zeile 4-14!!!!!!

#while 1==1:
    #print("Hilfe ich stecke Fest")
#_______________________________________________________________________________________________________________________
#for loop ein loop der eine bestimmte anzahl wiederholt wird
#for i in range(10):
    #print(i+1)

#for i in range (50,100+1,2): #(start,ende,schritte)
    #print(i)

for seconds in range(3,-3,-1):
    print(seconds)
    time.sleep(1)
print("Du hast echt geduld.")
#_______________________________________________________________________________________________________________________
#nested loops (ein loop in einem loop)

rows = int(input("Wie viele reihen soll das Quadrat haben?: "))
collums = int(input("Wie viele Zeilen soll es haben?: "))
zeichen = (input("Welches Zeichen soll verwendet werden?: "))

for i in range(rows):
    for j in range (collums):
        print(zeichen, end="")
    print()
#_______________________________________________________________________________________________________________________

while 1==1:
    print("Orthografitrainer ist kacke!")
    print("Die Deutsche Sprache macht micht Aggresiv!")
    print("Ich finde Sortieren langweilig!")

#_______________________________________________________________________________________________________________________


operandie = int(input("Wie willst du rechnen?(+ - / *): "))
zahl1 = int(input("Welche zahl?: "))
zahl2 = int(input("Soll mit welcher Zahl berechnet werden?: "))

if operandie =="+":
    print(int(zahl1)+int(zahl2))
elif operandie =="-":
    print(int(zahl1)-int(zahl2))
elif operandie =="*":
    print(int(zahl1)*int(zahl2))
elif operandie =="/":
    print(int(zahl1)/int(zahl2))
else:
    print("dann halt nicht")

#_______________________________________________________________________________________________________________________

vrank = None

while not vrank:
    vrank = input("Welchen Rank hast du in Valorant?: ")

if vrank =="Iron":
    print("Hör auf, auf die Füße zu schauen!")
elif vrank =="Bronze":
    print("Aimlabs = Free")
elif vrank =="Silver":
    print("Coachings + YT is free = KOMM IN DIE GRUPPE!")
elif vrank =="Gold":
    print("Hör auf zu fillen!")
elif vrank =="Platin":
    print("Dein Ego ist größer als meine Zukunft!")
elif vrank =="Diamond":
    print("Vllt mal Strats üben = Freelo")
elif vrank =="Ascendent":
    print("Hardstuck 4 Life UwU")
elif vrank =="Immortal":
    print("No Brain but aim/Dont cheat on your E-Kittens")
elif vrank =="Radiant":
    print("Touch Grass")
else:
    print("Uranked? ganz schön lame")
''' Visualisering av Gå-själv-program för åk 1-3 i 100 Innovationer.
(Möjligt att samma koncept går att använda för åk 4-6, men med texterna för "Allvetare".)
Programmet bygger på ett enkelt teknologiträd som elever bygger upp allt eftersom.
Det finns 28 innovationer delat på fyra grupper som var varsin färg: blå, grön, röd och gul.
Eleverna kommer få 7 olika val att göra där fyra innovationer presenteras (en från varje färg, 
helst i kronologisk ordning). De ska sedan hitta fram till innovationen i fråga, läsa "Små Genier"-texten
som hör till den och undersöka vilken färg innovationen har. Därefter återvänder de till läraren för att 
få en sådan i tygformat från läraren.'''

import turtle as T

green = 0
red = 0
yellow = 0
blue = 0

print("Du kommer nu att få bygga ditt eget teknologiträd, där olika innovationer kommer att presenteras för dig och beroende på vilket val du gör kommer du i slutet att hamna i en av fyra kategorier med tekniknördar.")
print("Om du har svårt att välja, eller om du inte vet vad en av innovationerna är för något, försök då hitta dem i utställningen så du kan läsa på om dem.")
print("\nPå den första raden i ditt teknologiträd kan du välja mellan")
print("a) Järnvägen, b) Vapen, c) Båten, eller d) Eldstaden")
firstChoice = input("Skriv in bokstaven 'a', 'b', 'c' eller 'd', beroende på ditt val: ")

print("\nPå den andra raden i ditt teknologiträd kan du välja mellan")
print("a) Diskmaskinen, b) Dynamiten, c) Spisen, eller d) Köksredskap")
secondChoice = input("Skriv in bokstaven 'a', 'b', 'c' eller 'd', beroende på ditt val: ")

print("\nPå den tredje raden i ditt teknologiträd kan du välja mellan")
print("a) Bilen, b) Motorcykeln, c) Cykeln, eller d) Sängen")
thirdChoice = input("Skriv in bokstaven 'a', 'b', 'c' eller 'd', beroende på ditt val: ")

print("\nPå den fjärde raden i ditt teknologiträd kan du välja mellan:")
print("a) Dammsugaren, b) Flyget, c) Kameran, eller d) Krutet")
fourthChoice = input("Skriv in bokstaven 'a', 'b', 'c' eller 'd', beroende på ditt val: ")

print("\nPå den femte raden i ditt teknologiträd kan du välja mellan")
print("a) Datorn, b) Mikrovågsugnen, c) Radion, eller d) Klockan")
fifthChoice = input("Skriv in bokstaven 'a', 'b', 'c' eller 'd', beroende på ditt val: ")

print("\nPå den sjätte raden i ditt teknologiträd kan du välja mellan")
print("a) Internet, b) Kärnkraft, c) Kylskåpet, eller d) Symaskinen")
sixthChoice = input("Skriv in bokstaven 'a', 'b', 'c' eller 'd', beroende på ditt val: ")

print("\nPå den sjunde raden i ditt teknologiträd kan du välja mellan")
print("a) Gpsen, b) Rymdraketen, c) Telefonen, eller d) Ångbrandsprutan")
seventhChoice = input("Skriv in bokstaven 'a', 'b', 'c' eller 'd', beroende på ditt val: ")



if firstChoice == "a":
	yellow += 1
elif firstChoice == "b":
	red += 1
elif firstChoice == "c":
	green += 1
elif firstChoice == "d":
	blue += 1
else:
	print("Det var inte ett giltigt val")
	
if secondChoice == "a":
	yellow += 1
elif secondChoice == "b":
	red += 1
elif secondChoice == "c":
	green += 1
elif secondChoice == "d":
	blue += 1
else:
	print("Det var inte ett giltigt val")
	
if thirdChoice == "a":
	yellow += 1
elif thirdChoice == "b":
	red += 1
elif thirdChoice == "c":
	green += 1
elif thirdChoice == "d":
	blue += 1
else:
	print("Det var inte ett giltigt val")
	
if fourthChoice == "a":
	yellow += 1
elif fourthChoice == "b":
	red += 1
elif fourthChoice == "c":
	green += 1
elif fourthChoice == "d":
	blue += 1
else:
	print("Det var inte ett giltigt val")
	
if fifthChoice == "a":
	yellow += 1
elif fifthChoice == "b":
	red += 1
elif fifthChoice == "c":
	green += 1
elif fifthChoice == "d":
	blue += 1
else:
	print("That was not a valid choice.")
	
if sixthChoice == "a":
	yellow += 1
elif sixthChoice == "b":
	red += 1
elif sixthChoice == "c":
	green += 1
elif sixthChoice == "d":
	blue += 1
else:
	print("Det var inte ett giltigt val")

if seventhChoice == "a":
	yellow += 1
elif seventhChoice == "b":
	red += 1
elif seventhChoice == "c":
	green += 1
elif seventhChoice == "d":
	blue += 1
else:
	print("Det var inte ett giltigt val")
	
print("\n\n\nDu fick " + str(yellow) + " gula pluppar. " + str(red) + " röda pluppar. " + str(green) + " gröna pluppar. Samt " + str(blue) + " blå pluppar.\n")

if yellow >= blue and yellow >= red and yellow >= green:
	print("Du är en riktig tekniknörd! Men tänk på att miljön tar skada av en del av den teknik vi uppfunnit. Fundera noga på hur du använder dig av tekniken och undersök om det finns bättre sätt att göra saker på.")
	colour = "yellow"
	
elif blue >= yellow and blue >= red and blue >= green:
	print("Du är inte först i kön när Apple släpper en ny telefon direkt. Gillar du ens teknik? Mycket av den värld har runt oss idag finns tack vare ny teknik, du borde ge det en chans!")
	colour = "blue"
	
elif red >= yellow and red >= blue and red >= green:
	print("Oj då! Ny teknik är det du lever för och du drar dig inte för att vara före testpiloterna. Tänk på att inte all teknik är säker och att en del ny teknik bör hanteras varsamt, annars kan det gå illa!")
	colour="red"
	
else:
	print("Du följer med teknikförändringen i världen, men vill inte gärna prova på något själv, det lämnar du åt andra. När en ny teknikpryl testats av generationer, då vågar också du börjar använda sakerna.")
	colour="green"

T.color(colour)
T.sety(-400)
T.begin_fill()
T.circle(400)
T.end_fill()
# !python

# Vad behöver vi?:
# En variabel för datorn, som kan slumpa fram ett värde mellan 0 och 2
# Conditionals som väljer ut en sten, sax eller påse beroende på vilken
# siffra som slumpats fram.
# En input som låter spelaren välja sten, sax eller påse
# En input som låter spelaren välja bästa av 3,5,7 eller 9
# Poängvariabler för spelaren och datorn

# TODO: Lägg till en liten AI för datorns val. Typ:
# Om båda valda samma en omgång, välj samma igen
# Om du vann med sax, välj påse nästa gång, etc.

import random

playTime = int(input("Ska spelet pågå i 3, 5, 7 eller 9 omgångar?: ") )
playerNumber = 0
roundsPlayed = 0
roundsRemaining = 0
playerPoints = 0
compPoints = 0
leaderPoints = 0

# Kontrollerar om det fortfarande finns en chans att vinna.
''' Får inte ha "break" utanför en loop tydligen...
def roundsCheck():
	if playTime == 3 and (playerPoints or compPoints == 2):
		break
	elif playTime == 5 and (playerPoints or compPoints == 3):
		break
	elif playTime == 7 and (playerPoints or compPoints == 4):
		break
	elif playTime == 9 and (playerPoints or compPoints == 5):
		break'''

if playTime > 9:
	print("Så länge vill vi inte spela!")
elif playTime not in [3,5,7,9]:
	print(str(playTime) + " är ett jämnt tal. Vi vill ha en vinnare och det kan inte garanteras om det är jämnt antal spelomgångar!")

while roundsPlayed < playTime:
	playerInput = str.upper(input("Välj sten, sax eller påse!: ") )
	compRand = random.randrange(2)
	
	if playerInput == "STEN":
		playerNumber = 0
	elif playerInput == "SAX":
		playerNumber = 1
	elif playerInput == "PÅSE":
		playerNumber = 2
	else:
		print("Du måste skriva in 'sten', 'sax' eller 'påse'!\n")
		
	if playerNumber < compRand:
		if playerInput == "STEN":
			print("Påse tar sten, datorn tar poäng!")
		elif playerInput == "SAX":
			print("Sten tar sax, datorn tar poäng!")
		else:
			print("Sax tar påse, datorn tar poäng!")
		
		compPoints += 1
	elif playerNumber > compRand:
		if playerInput == "STEN":
			print("Sten tar sax, du vann den här omgången!")
		elif playerInput == "SAX":
			print("Sax tar påse, du vann den här omgången!")
		else:
			print("Påse tar sten, du vann den här omgången!")
		
		playerPoints += 1
	else:
		print("Ni valde " + playerInput + " båda två!")
		roundsPlayed -= 1
		
	# Visar och håller reda på ledaren
	if playerPoints > compPoints:
		leaderPoints = playerPoints
		print("Du leder med " + str(playerPoints-compPoints) + " poäng.")
	elif compPoints > playerPoints:
		leaderPoints = compPoints
		print("Datorn leder med " + str(compPoints-playerPoints) + " poäng.")
	else:
		print("Ställningen är lika.")
		
	roundsPlayed += 1
	roundsRemaining = playTime-roundsPlayed
	
	'''# Visar hur många omgångar som återstår
	if roundsRemaining is not 1:
		print("Det är " + str(roundsRemaining) + " omgångar kvar.")
	else:
		print("Det är " + str(roundsRemaining) + " omgång kvar.")'''
	
	# Avbryter loopen om det inte finns någon chans att den som ligger under kan vinna längre.
	''' Bättre lösning på detta finns nedan
	if playTime == 3 and leaderPoints == 2:
		break
	elif playTime == 5 and leaderPoints == 3:
		break
	elif playTime == 7 and leaderPoints == 4:
		break
	elif playTime == 9 and leaderPoints == 5:
		break'''
		
	if (float(leaderPoints)/float(playTime) ) > 0.5:
		break
	
if playerPoints > compPoints:
	print("\nGrattis, du vann med ledningen " + str(playerPoints) + " mot " + str(compPoints) )
elif compPoints > playerPoints:
	print("\nDu förlorade! Datorn vann med " + str(compPoints) + " poäng mot dina " + str(playerPoints) )
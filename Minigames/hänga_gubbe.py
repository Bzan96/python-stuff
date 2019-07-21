# !python

# Vi behöver:
# En variabel som håller ordet som spelaren ska gissa sig fram till
# En variabel som håller redan på den gissade bokstaven
# Variabler som håller reda på hur många rätt gissningar man gjort, samt vinst


inputWord = str.upper(input("Skriv in ordet som spelaren ska gissa på: ") )
guessedLetter = ""
wordLength = len(inputWord)
wordList = [""] * wordLength
usedLetters = [""]

letterNumber = 0
allowedGuesses = 10
rightGuesses = 0
winGuesses = 0

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("Ordet du ska gissa dig fram till är " + str(wordLength) + " bokstäver långt.")
print("Du har 10 gissningar på dig, lycka till! Skriv 'END' för att avsluta.")

while(guessedLetter != "END") and (allowedGuesses != 0):
	print(wordList)
	print("Du har " + str(allowedGuesses) + " gissningar kvar.")
	guessedLetter = str.upper(input("Gissa på en bokstav: ") )
	
	while letterNumber < wordLength:
		if guessedLetter in usedLetters:
			print("Du har redan gissat på den bokstaven.")
			allowedGuesses +=1
			break
		
		elif inputWord[letterNumber] == guessedLetter:
			wordList[letterNumber] = guessedLetter
			rightGuesses = 1
			winGuesses += 1
		
		letterNumber += 1
	
	allowedGuesses -= 1-rightGuesses
	rightGuesses = 0
	letterNumber = 0
	
	usedLetters.append(guessedLetter)
	
	if winGuesses == len(inputWord):
		print(wordList)
		print("Woho, du vann! Det rätta ordet var " + inputWord)
		break
	elif allowedGuesses == 0:
		print("Du har inga fler gissningar! Det rätta ordet var " + inputWord)
		break
	elif guessedLetter == "END":
		break
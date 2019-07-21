# !python

# Vi behöver:
# En lista som håller den rätta kombinationen
# En lista för datorn som märker ut rätt och fel pluppar
# En lista för spelaren som håller de rätta svaren
# En annan lista för spelaren där man skriver i sina gissningar

import random

startDot = 0

rightComb = ["."]*4
randComb = []
compMarks = []*4
playerComb = [""]*4
rightGuesses = [""]*4

# Stora pluppar: Blå, Gula, Lila, Gröna, Svarta
# Små pluppar: Vita, Röda


for i in range(4):
	startDot = random.randrange(5)
	print(startDot)
	randComb.append(startDot)
		
		
		# UÄÄÄÄÄÄÄHHHHHHHHHHHH
	if randComb[startDot] == randComb(0):
		rightComb = str.replace(rightComb["."],rightComb["Blå"])
	elif randComb[startDot] == randComb(1):
		rightComb = str.replace(rightComb["."],rightComb["Gul"])
	elif randComb[startDot] == randComb(2):
		rightComb = str.replace(rightComb["."],rightComb["Lila"])
	elif randComb[startDot] == randComb(3):
		rightComb = str.replace(rightComb["."],rightComb["Grön"])
	elif randComb[startDot] == randComb(4):
		rightComb = str.replace(rightComb["."],rightComb["Svart"])

print(randComb)
print(rightComb)
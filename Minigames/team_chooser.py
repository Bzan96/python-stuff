from random import choice
import os

path = "C:/Users/bzan9/Desktop/Python/Minigames"

os.chdir( path )

##players = ["Crosby", "Malkin", "Kessel", "Letang", "Dumolin", "Murray",
##"Ovechkin", "Kuznetzov", "Backstrom", "Niskanen", "Carlson", "Holtby"]
players = []
team_names = []

playerFile = open("players.txt", "r")
teamFile = open("teams.txt", "r")
players = playerFile.read().splitlines()
team_names = teamFile.read().splitlines()

teamA = []
teamB = []
teamC = []
teamD = []

while len(players) > 0:
	playerA = choice(players)
	teamA.append(playerA)
	players.remove(playerA)
	
	if players == []:
		break
	
	playerB = choice(players)
	teamB.append(playerB)	
	players.remove(playerB)

	if players == []:
		break
	
	playerC = choice(players)
	teamC.append(playerC)	
	players.remove(playerC)
	
	if players == []:
		break
	
	playerD = choice(players)
	teamD.append(playerD)	
	players.remove(playerD)
	
team = choice(team_names)
print(str(team) + ":\n")
team_names.remove(team)
for i in teamA:
	print(i)
	
print("\n")

team = choice(team_names)
print(str(team) + ":\n")
team_names.remove(team)	
for i in teamB:
	print(i)
	
print("\n")

team = choice(team_names)
print(str(team) + ":\n")
team_names.remove(team)
for i in teamC:
	print(i)
	
print("\n")
	
team = choice(team_names)
print(str(team) + ":\n")
for i in teamD:
	print(i)
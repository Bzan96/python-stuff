# !python

# We need:
# A list with property-value-pairs holding all the cards
# A variable holding the current hand of player 1, 2, 3 and 4
# A variable for the card-choice of the player
# A variable holding the current hand of the House
# The Houses loses even if all player rise above 21, fix that!

import random

# In BlackJack, Jack, Queen and King are counted as 10s
cardList = {2:4, 3:4, 4:4, 5:4, 6:4, 7:4, 8:4, 9:4, 10:16, 11:4}

players = int(input("How many people will be playing (1-4)? ") )
# hands = ["houseHand":0, "pOneHand":0, "pTwoHand":0, "pThreeHand":0, "pFourHand":0]
# choices = ["pOneChoice", "pTwoChoice", "pThreeChoice", "pFourChoice"]

pOneHand = 0
pOneChoice = ""
pTwoHand = 0
pTwoChoice = ""
pThreeHand = 0
pThreeChoice = ""
pFourHand = 0
pFourChoice = ""
houseHand = 0
round = 0
playerInput = ""
gameOver = False

while playerInput != "END" and gameOver == False:
	if players != 1:
		print("\nThe game will start with " + str(players) + " players and the House.")
		for i in range(2):
			# Chooses a card between 2 and 14
			p1add = random.randrange(2,11)
			p2add = random.randrange(2,11)
			p3add = random.randrange(2,11)
			p4add = random.randrange(2,11)
			# Adds the chosen card to the player's hand
			pOneHand += p1add
			pTwoHand += p2add
			pThreeHand += p3add
			pFourHand += p4add
			# Removes the chosen card from available cards
			cardList[p1add] -= 1
			cardList[p2add] -= 1
			cardList[p3add] -= 1
			cardList[p4add] -= 1
		
		# The House card addition runs once in the outside loot so it cannot be in the for-loop
		hAdd = random.randrange(2,11)
		houseHand += hAdd
		cardList[hAdd] -= 1		
	else:
		print("\nThe game will start with " + str(players) + " player and the House.")
		for i in range(2):
			p1add = random.randrange(2,11)
			cardList[p1add] -= 1
			pOneHand += p1add
		
		# The House card addition runs once in the outside loot so it cannot be in the for-loop
		hAdd = random.randrange(2,11)
		houseHand += hAdd
		cardList[hAdd] -= 1
	print("Your goal is to get as close to 21 as possible, but not above. Good luck!")
	
	while(houseHand < 22):
		round += 1
		print("\n === Round " + str(round) + " === ")
		
		# Conditionals for 1 player
		if players == 1:
			print(cardList)
			
			if pOneHand <= 21:
				print("\nPlayer 1's current hand is at " + str(pOneHand) + ", how will you proceed?")
				pOneChoice = str.lower(input("Do you want to 'a' (add) a card or 'p'? ") )
			else:
				pOneChoice = "p"
			
			if pOneHand == 21:
				print("You won! Congratulations!")
				gameOver = True
				break
			elif pOneChoice == "p":
				pOneHand += 0
			elif pOneChoice == "a":
				p1add = random.randrange(2,11)
				pOneHand += p1add
				cardList[p1add] -= 1
				print("You drew the " + str(p1add) + "-card.")
			else:
				print("That is not possible.")
				round -= 1
		# Conditionals for 2 players
		elif players == 2:
			if pOneHand == 21:
				print("Player 1 won! Congratulations!")
				gameOver = True
				break
			elif pTwoHand == 21:
				print("Player 2 won! Congratulations!")
				gameOver = True
				break
			
			if pOneHand <= 21:
				print("\nPlayer 1's current hand is at " + str(pOneHand) + ", how will you proceed?")
				pOneChoice = str.lower(input("Do you want to 'a' (add) a card or 'p' (pass)? ") )
			else:
				pOneChoice = "p"
			if pTwoHand <= 21:
				print("Player 2's current hand is at " + str(pTwoHand) + ", how will you proceed?")
				pTwoChoice = str.lower(input("Do you want to 'a' (add) a card or 'p' (pass)? ") )
			else:
				pTwoChoice = "p"
			
			# If both pass
			if pOneChoice == "p" and pTwoChoice == "p":
				pOneHand += 0
				pTwoHand += 0
			elif pOneChoice == "p" and pTwoChoice == "a":
				pOneHand += 0
				
				pTwoHand += p2add
				p2add = random.randrange(2,11)		
				cardList[p2add] -= 1
				print("Player 2 drew the " + str(p2add) + "-card.")
			elif pOneChoice == "a" and pTwoChoice == "p":
				pOneHand += p1add
				p1add = random.randrange(2,11)		
				cardList[p1add] -= 1
				
				pTwoHand += 0
				print("Player 1 drew the " + str(p1add) + "-card.")
			# If both adds
			elif pOneChoice == "a" and pTwoChoice == "a":
				pOneHand += p1add
				p1add = random.randrange(2,11)		
				cardList[p1add] -= 1
				
				pTwoHand += p2add
				p2add = random.randrange(2,11)		
				cardList[p2add] -= 1
				print("Player 1 drew the " + str(p1add) + "-card.")
				print("Player 2 drew the " + str(p2add) + "-card.")
			else:
				print("That is not possible.")
				round -= 1
		# Conditionals for 3 players
		elif players == 3:
			if pOneHand == 21:
				print("Player 1 won! Congratulations!")
				gameOver = True
				break
			elif pTwoHand == 21:
				print("Player 2 won! Congratulations!")
				gameOver = True
				break
			elif pThreeHand == 21:
				print("Player 3 won! Congratulations!")
				gameOver = True
				break
			
			if pOneHand <= 21:
				print("\nPlayer 1's current hand is at " + str(pOneHand) + ", how will you proceed?")
				pOneChoice = str.lower(input("Do you want to 'a' (add) a card or 'p' (pass)? ") )
			else:
				pOneChoice = "p"
			if pTwoHand <= 21:
				print("Player 2's current hand is at " + str(pTwoHand) + ", how will you proceed?")
				pTwoChoice = str.lower(input("Do you want to 'a' (add) a card or 'p' (pass)? ") )
			else:
				pTwoChoice = "p"
			if pThreeHand <= 21:
				print("Player 3's current hand is at " + str(pThreeHand) + ", how will you proceed?")
				pThreeChoice = str.lower(input("Do you want to 'a' (add) a card or 'p' (pass)? ") )
			else:
				pThreeChoice = "p"
			
			# If everyone passes
			if pOneChoice == "p" and pTwoChoice == "p" and pThreeChoice == "p":
				pOneHand += 0
				pTwoHand += 0
				pThreeHand += 0
			# If everyone adds
			elif pOneChoice == "a" and pTwoChoice == "a" and pThreeChoice == "a":
				pOneHand += p1add
				p1add = random.randrange(2,11)		
				cardList[p1add] -= 1
				
				pTwoHand += p2add
				p2add = random.randrange(2,11)		
				cardList[p2add] -= 1

				pThreeHand += p3add
				p3add = random.randrange(2,11)		
				cardList[p3add] -= 1
				print("Player 1 drew the " + str(p1add) + "-card.")
				print("Player 2 drew the " + str(p2add) + "-card.")
				print("Player 3 drew the " + str(p3add) + "-card.")				
			# If player 3 choice is "pass" but the other two vary
			elif pOneChoice == "p" and pTwoChoice == "a" and pThreeChoice == "p":
				pOneHand += 0
				
				pTwoHand += p2add
				p2add= random.randrange(2,11)		
				cardList[p2add] -= 1
				
				pThreeHand += 0
				print("Player 2 drew the " + str(p2add) + "-card.")
			elif pOneChoice == "a" and pTwoChoice == "p" and pThreeChoice == "p":
				pOneHand += p1add
				p1add = random.randrange(2,11)		
				cardList[p1add] -= 1

				pTwoHand += 0
				pThreeHand += 0
				print("Player 1 drew the " + str(p1add) + "-card.")
			elif pOneChoice == "a" and pTwoChoice == "a" and pThreeChoice == "p":
				pOneHand += p1add
				p1add = random.randrange(2,11)		
				cardList[p1add] -= 1
				
				pTwoHand += p2add
				p2add = random.randrange(2,11)		
				cardList[p2add] -= 1
				
				pThreeHand += 0
				print("Player 1 drew the " + str(p1add) + "-card.")
				print("Player 2 drew the " + str(p2add) + "-card.")
			
			# If player 2 choice is "pass"
			elif pOneChoice == "p" and pTwoChoice == "p" and pThreeChoice == "a":
				pOneHand += 0
				pTwoHand += 0
				
				pThreeHand += p3add
				p3add = random.randrange(2,11)		
				cardList[p3add] -= 1
				print("Player 3 drew the " + str(p3add) + "-card.")
			elif pOneChoice == "a" and pTwoChoice == "p" and pThreeChoice == "p":
				pOneHand += p1add
				p1add = random.randrange(2,11)		
				cardList[p1add] -= 1
				
				pTwoHand += 0
				pThreeHand += 0
				print("Player 1 drew the " + str(p1add) + "-card.")
			elif pOneChoice == "a" and pTwoChoice == "p" and pThreeChoice == "a":
				pOneHand += p1add
				p1add = random.randrange(2,11)		
				cardList[p1add] -= 1

				pTwoHand += 0

				pThreeHand += p3add
				p3add = random.randrange(2,11)		
				cardList[p3add] -= 1
				print("Player 1 drew the " + str(p1add) + "-card.")
				print("Player 3 drew the " + str(p3add) + "-card.")
			
			# If player 1 choice is "pass"
			elif pOneChoice == "p" and pTwoChoice == "a" and pThreeChoice == "p":
				pOneHand += 0
				
				pTwoHand += p2add
				p2add = random.randrange(2,11)		
				cardList[p2add] -= 1
				
				pThreeHand += 0
				print("Player 2 drew the " + str(p2add) + "-card.")
			elif pOneChoice == "p" and pTwoChoice == "p" and pThreeChoice == "a":
				pOneHand += 0
				pTwoHand += 0
				
				pThreeHand += p3add
				p3add = random.randrange(2,11)		
				cardList[p3add] -= 1
				print("Player 3 drew the " + str(p3add) + "-card.")
			elif pOneChoice == "p" and pTwoChoice == "a" and pThreeChoice == "a":
				pOneHand += 0
				pTwoHand += p2add
				pThreeHand += p3add
				print("Player 3 drew the " + str(p3add) + "-card.")
				print("Player 2 drew the " + str(p2add) + "-card.")
			else:
				print("That is not possible.")
				round -= 1
		# Conditionals for 4 players
		elif players == 4:
			if pOneHand == 21:
				print("Player 1 won! Congratulations!")
				gameOver = True
				break
			elif pTwoHand == 21:
				print("Player 2 won! Congratulations!")
				gameOver = True
				break
			elif pThreeHand == 21:
				print("Player 3 won! Congratulations!")
				gameOver = True
				break
			elif pFourHand == 21:
				print("Player 4 won! Congratulations!")
				gameOver = True
				break
	
			if pOneHand <= 21:
				print("\nPlayer 1's current hand is at " + str(pOneHand) + ", how will you proceed?")
				pOneChoice = str.lower(input("Do you want to 'a' (add) a card or 'p' (pass)? ") )
			else:
				pOneChoice = "p"
			if pTwoHand <= 21:
				print("Player 2's current hand is at " + str(pTwoHand) + ", how will you proceed?")
				pTwoChoice = str.lower(input("Do you want to 'a' (add) a card or 'p' (pass)? ") )
			else:
				pTwoChoice = "p"
			if pThreeHand <= 21:
				print("Player 3's current hand is at " + str(pThreeHand) + ", how will you proceed?")
				pThreeChoice = str.lower(input("Do you want to 'a' (add) a card or 'p' (pass)? ") )
			else:
				pThreeChoice = "p"
			if pFourHand <= 21:
				print("Player 4's current hand is at " + str(pFourHand) + ", how will you proceed?")
				pFourChoice = str.lower(input("Do you want to 'a' (add) a card or 'p' (pass)? ") )
			else:
				pFourChoice = "p"
					
			# If everyone passes
			if pOneChoice == "p" and pTwoChoice == "p" and pThreeChoice == "p" and pFourChoice == "p":
				pOneHand += 0
				pTwoHand += 0
				pThreeHand += 0
				pFourHand += 0
			# If everyone adds
			elif pOneChoice == "a" and pTwoChoice == "a" and pThreeChoice == "a" and pFourChoice == "a":
				pOneHand += p1add
				p1add = random.randrange(2,11)		
				cardList[p1add] -= 1

				pTwoHand += p2add
				p2add = random.randrange(2,11)		
				cardList[p2add] -= 1

				pThreeHand += p3add
				p3add = random.randrange(2,11)		
				cardList[p3add] -= 1

				pFourHand += p4add
				p4add = random.randrange(2,11)		
				cardList[p4add] -= 1
				print("Player 1 drew the " + str(p1add) + "-card.")
				print("Player 2 drew the " + str(p2add) + "-card.")
				print("Player 3 drew the " + str(p3add) + "-card.")
				print("Player 4 drew the " + str(p3add) + "-card.")				
			# If player 4 choice is "pass" but the other three vary
			# The hexadecimal system gives 7 alternatives where player 4 passes, when "all adds" and "all passes" are taken away
			# 0010
			elif pOneChoice == "p" and pTwoChoice == "p" and pThreeChoice == "a" and pFourChoice == "p":
				pOneHand += 0
				pTwoHand += 0
				
				pThreeHand += p3add
				p3add = random.randrange(2,11)		
				cardList[p3add] -= 1

				pFourHand += 0
				print("Player 3 drew the " + str(p3add) + "-card.")
			# 0100
			elif pOneChoice == "p" and pTwoChoice == "a" and pThreeChoice == "p" and pFourChoice == "p":
				pOneHand += 0
				
				pTwoHand += p2add
				p2add = random.randrange(2,11)		
				cardList[p2add] -= 1

				pThreeHand += 0
				pFourHand += 0
				print("Player 2 drew the " + str(p2add) + "-card.")
			# 0110
			elif pOneChoice == "p" and pTwoChoice == "a" and pThreeChoice == "a" and pFourChoice == "p":
				pOneHand += 0
				
				pTwoHand += p2add
				p2add = random.randrange(2,11)		
				cardList[p2add] -= 1

				pThreeHand += p3add
				p3add = random.randrange(2,11)		
				cardList[p3add] -= 1

				pFourHand += 0
				print("Player 2 drew the " + str(p2add) + "-card.")
				print("Player 3 drew the " + str(p3add) + "-card.")
			# 1000
			elif pOneChoice == "a" and pTwoChoice == "p" and pThreeChoice == "p" and pFourChoice == "p":
				pOneHand += p1add
				p1add = random.randrange(2,11)		
				cardList[p1add] -= 1

				pTwoHand += 0
				pThreeHand += 0
				pFourHand += 0
				print("Player 1 drew the " + str(p1add) + "-card.")
			# 1010
			elif pOneChoice == "a" and pTwoChoice == "p" and pThreeChoice == "a" and pFourChoice == "p":
				pOneHand += p1add
				p1add = random.randrange(2,11)		
				cardList[p1add] -= 1

				pTwoHand += 0

				pThreeHand += p3add
				p3add = random.randrange(2,11)		
				cardList[p3add] -= 1

				pFourHand += 0
				print("Player 1 drew the " + str(p1add) + "-card.")
				print("Player 3 drew the " + str(p3add) + "-card.")
			# 1100
			elif pOneChoice == "a" and pTwoChoice == "a" and pThreeChoice == "p" and pFourChoice == "p":
				pOneHand += p1add
				p1add = random.randrange(2,11)		
				cardList[p1add] -= 1

				pTwoHand += p2add
				p2add = random.randrange(2,11)		
				cardList[p2add] -= 1

				pThreeHand += 0
				pFourHand += 0
				print("Player 1 drew the " + str(p1add) + "-card.")
				print("Player 2 drew the " + str(p2add) + "-card.")
			# 1110
			elif pOneChoice == "a" and pTwoChoice == "a" and pThreeChoice == "a" and pFourChoice == "p":
				pOneHand += p1add
				p1add = random.randrange(2,11)		
				cardList[p1add] -= 1

				pTwoHand += p2add
				p2add = random.randrange(2,11)		
				cardList[p2add] -= 1

				pThreeHand += p3add
				p3add = random.randrange(2,11)		
				cardList[p3add] -= 1

				pFourHand += 0
				print("Player 1 drew the " + str(p1add) + "-card.")
				print("Player 2 drew the " + str(p2add) + "-card.")
				print("Player 3 drew the " + str(p3add) + "-card.")
			# If player 3 choice is "pass" but the other three vary
			# The hexadecimal system gives 4 possible alternatives left when both player 3 passes but player 4 doesn't
			# 0001
			elif pOneChoice == "p" and pTwoChoice == "p" and pThreeChoice == "p" and pFourChoice == "a":
				pOneHand += 0
				pTwoHand += 0
				pThreeHand += 0
				
				pFourHand += p4add
				p4add = random.randrange(2,11)		
				cardList[p4add] -= 1
				print("Player 4 drew the " + str(p4add) + "-card.")
			# 0101
			elif pOneChoice == "p" and pTwoChoice == "a" and pThreeChoice == "p" and pFourChoice == "a":
				pOneHand += 0
				
				pTwoHand += p2add
				p2add = random.randrange(2,11)		
				cardList[p2add] -= 1
				
				pThreeHand += 0
				
				pFourHand += p4add
				p4add = random.randrange(2,11)		
				cardList[p4add] -= 1
				print("Player 2 drew the " + str(p2add) + "-card.")
				print("Player 4 drew the " + str(p4add) + "-card.")
			# 1001
			elif pOneChoice == "a" and pTwoChoice == "p" and pThreeChoice == "p" and pFourChoice == "a":
				pOneHand += p1add
				p1add = random.randrange(2,11)		
				cardList[p1add] -= 1

				pTwoHand += 0
				pThreeHand += 0
				
				pFourHand += p4add
				p4add = random.randrange(2,11)		
				cardList[p4add] -= 1
				print("Player 1 drew the " + str(p1add) + "-card.")
				print("Player 4 drew the " + str(p4add) + "-card.")
			# 1101
			elif pOneChoice == "a" and pTwoChoice == "a" and pThreeChoice == "p" and pFourChoice == "a":
				pOneHand += p1add
				p1add = random.randrange(2,11)		
				cardList[p1add] -= 1
				
				pTwoHand += p2add
				p2add = random.randrange(2,11)		
				cardList[p2add] -= 1

				pThreeHand += 0
				
				pFourHand += p4add
				p4add = random.randrange(2,11)		
				cardList[p4add] -= 1
				print("Player 1 drew the " + str(p1add) + "-card.")
				print("Player 2 drew the " + str(p2add) + "-card.")
				print("Player 4 drew the " + str(p4add) + "-card.")
			# If player 2 choice is "pass" but the other three vary
			# The hexadecimal system gives 2 possible alternatives left at this point
			# 1011
			elif pOneChoice == "a" and pTwoChoice == "p" and pThreeChoice == "a" and pFourChoice == "a":
				pOneHand += p1add
				p1add = random.randrange(2,11)		
				cardList[p1add] -= 1

				pTwoHand += 0

				pThreeHand += p3add
				p3add = random.randrange(2,11)		
				cardList[p3add] -= 1
				
				pFourHand += p4add
				p4add = random.randrange(2,11)		
				cardList[p4add] -= 1
				print("Player 1 drew the " + str(p1add) + "-card.")
				print("Player 3 drew the " + str(p3add) + "-card.")
				print("Player 4 drew the " + str(p4add) + "-card.")
			# 0011
			elif pOneChoice == "p" and pTwoChoice == "p" and pThreeChoice == "a" and pFourChoice == "a":
				pOneHand += 0
				pTwoHand += 0
				
				pThreeHand += p3add
				p3add = random.randrange(2,11)		
				cardList[p3add] -= 1

				pFourHand += p4add
				p4add = random.randrange(2,11)		
				cardList[p4add] -= 1
				print("Player 3 drew the " + str(p3add) + "-card.")
				print("Player 4 drew the " + str(p4add) + "-card.")
			# If player 1 choice is "pass" but the other three vary
			# The hexadecimal system leaves 1 possible alternative
			# 0111
			elif pOneChoice == "p" and pTwoChoice == "a" and pThreeChoice == "a" and pFourChoice == "a":
				pOneHand += 0
				
				pTwoHand += p2add
				p2add = random.randrange(2,11)		
				cardList[p2add] -= 1

				pThreeHand += p3add
				p3add = random.randrange(2,11)		
				cardList[p3add] -= 1

				pFourHand += p4add
				p4add = random.randrange(2,11)		
				cardList[p4add] -= 1
				print("Player 2 drew the " + str(p2add) + "-card.")
				print("Player 3 drew the " + str(p3add) + "-card.")
				print("Player 4 drew the " + str(p4add) + "-card.")
			else:
				print("That is not possible.")
				round -= 1
		
		hAdd = random.randrange(2,11)
		houseHand += hAdd
		cardList[hAdd] -= 1
		
		# If user input is wrong
		if (pOneChoice or pTwoChoice or pThreeChoice or pFourChoice) not in ["p", "a"]:
			houseHand -= hAdd
		elif houseHand == 21:
			print("The House is at " + str(houseHand) )
			print("The House wins! You've lost all your savings, losers!")
			gameOver = True
			break		
		# Not perfect as of now. If the House loses with one or more players at the same amount,
		# the first player listed wins = unfair.
		elif houseHand > 21:
			print("The House is at " + str(houseHand) + ", which is over 21.")
			print("The House lost!")
			
			winList = {"Player 1":pOneHand, "Player 2":pTwoHand, "Player 3":pThreeHand, "Player 4":pFourHand}
			sortedList = [(v,k) for k,v in winList.items() ]
			sortedList.sort(reverse=True)
			for v,k in sortedList:
				print("%s" % (k) + " is your winner with %d" % (v) + " points!")
				break

			'''if pOneHand >= (pTwoHand and pThreeHand and pFourHand) and pOneHand < 22:
				print("Player 1's hand is at " + str(pOneHand) )
				print("Player 1 wins! Congratulations!")
			elif pTwoHand >= (pOneHand and pThreeHand and pFourHand) and pTwoHand < 22:
				print("Player 2's hand is at " + str(pTwoHandHand) )
				print("Player 2 wins! Congratulations!")
			elif pThreeHand >= (pTwoHand and pOneHand and pFourHand) and pThreeHand < 22:
				print("Player 3's hand is at " + str(pThreeHand) )
				print("Player 3 wins! Congratulations!")
			elif pFourHand >= (pTwoHand and pOneHand and pThreeHand) and pFourHand < 22:
				print("Player 4's hand is at " + str(pFourHandHand) )
				print("Player 4 wins! Congratulations!")'''
			gameOver = True
			break
		else:
			playerScores = {"Player 1":pOneHand, "Player 2":pTwoHand, "Player 3":pThreeHand, "Player 4":pFourHand}
			print("The House's hand is at " + str(houseHand) )
			print(playerScores)
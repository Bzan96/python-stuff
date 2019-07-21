#!/bin/python3

# Replace RPG starter project with this code when new instructions are live

def showInstructions():
  #print a main menu and the commands
  print('''
RPG Game
========

Get to the Garden with a key and a potion
Avoid the monsters!

Most of the items are just for fun, but the razor will save your life!

Commands:
  go [direction]
  get [item]
''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
rooms = {

	'Hall' : { 
		'north' : 'Bedroom',
		'south' : 'Kitchen',
		'east' : 'Dining Room',
		'item' : 'key'
	},
	
	"Bedroom" : {
		"south" : "Hall",
		"east" : "Toilet",
		'item' : 'soft pillow'
	},
	
	"Toilet" : {
		"west" : "Bedroom",
		"east" : "Master Bedroom",
		"south" : "Dining Room",
		"item" : "razor blade"
	},
	
	"Master Bedroom" : {
		"west" : "Toilet",
		"south" : "Man Cave",
		"item" : "bedpost"
	},
	
	"Man Cave" : {
		"north" : "Master Bedroom",
		"west" : "Living Room",
		"south" : "Garden",
		"item" : "sex doll"
	},
	
	"Garden" : {
		"north" : "Man Cave",
		"item" : ""
	},
	
	'Kitchen' : {
		'north' : 'Hall',
		'east' : 'Living Room',
		'item' : 'cookie monster'
	},
	
	'Dining Room' : {
		'west' : 'Hall',
		'south' : 'Living Room',
		"north" : "Toilet",
		'item' : 'monster'
	},
	
	'Living Room' : {
		'north' : 'Dining Room',
		'west' : 'Kitchen',
		"east" : "Man Cave",
		'item' : 'potion'
	},
}

#start the player in the Hall
currentRoom = 'Hall'

showInstructions()

#loop forever
while True:

	showStatus()

	#get the player's next 'move'
	#.split() breaks it up into an list array
	#eg typing 'go east' would give the list:
	#['go','east']
	move = ''
	while move == '':  
		move = input('>')

		move = move.lower().split()

		#if they type 'go' first
		if move[0] == 'go':
			#check that they are allowed wherever they want to go
			if move[1] in rooms[currentRoom]:
				#set the current room to the new room
				currentRoom = rooms[currentRoom][move[1]]
			#there is no door (link) to the new room
			else:
				print('You can\'t go that way!')

	#if they type 'get' first
	if move[0] == 'get' :
		#if the room contains an item, and the item is the one they want to get
		if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
			#add the item to their inventory
			inventory += [move[1]]
			#display a helpful message
			print(move[1] + ' got!')
			#delete the item from the room
			del rooms[currentRoom]['item']
			#otherwise, if the item isn't there to get
		else:
			#tell them they can't get it
			print('Can\'t get ' + move[1] + '!')

	# player loses if they enter a room with a monster
	if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
		if "razor" in inventory:
			print("There was a monster in that room, but thankfully your newly acquired razor saved you!")
		else:
			print("The cookie monster got you... GAME OVER!")
			break
		
	elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
		if "razor" in inventory:
			print("There was a monster in that room, but thankfully your newly acquired razor saved you!")
		else:
			print("The cookie monster got you... GAME OVER!")
			break
			
		
	# player wins the game if they get to the garden with a key and a shield
	if currentRoom == "Garden" and "key" in inventory and "potion" in inventory:
		print("You escaped the house... YOU WIN!")
		break
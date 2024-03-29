import os
from turtle import *
from random import choice

path = "C:/Users/bzan9/Desktop/Python/Minigames"
os.chdir( path )

screen = Screen()
screen.bgcolor("white")
penup()
hideturtle()

robots = {}

file = open("cards.txt", "r")
for line in file.read().splitlines():
	name, battery, intelligence, image = line.split(", ")
	robots[name] = [battery, intelligence, image]
	screen.register_shape(image)
file.close()

while True:
	robot = input("Choose a robot: ")
	
	if robot in robots:
		stats = robots[robot]
		style = ("Courier", 18, "italic")
		clear()
		goto(0, 100)
		shape(stats[2])
		setheading(90)
		stamp()
		setheading(-90)
		forward(60)
		write("Name: " + robot, font=style, align="center")
		forward(25)
		write("Battery: " + stats[0], font=style, align="center")
		forward(25)
		write("Intelligence: " + stats[1], font=style, align="center")
		
	elif robot == "random":
		robot = choice(list(robots.keys() ) )
		print(robot)
		
	else:
		print("Robot does\'t exist!")
		
		
from turtle import *
from random import *

colormode(255)
speed(0)

def randomcolour():
	red = randint(0,255)
	green = randint(0,255)
	blue = randint(0,255)
	color(red, green, blue)

def randomplace():
	penup()
	x = randint(-250, 250)
	y = randint(-250, 250)
	goto(x, y)
	pendown()
	
def randomheading():
	z = randint(1, 360)
	setheading(z)

def drawrectangle():
	randomcolour()
	randomplace()
	hideturtle()
	length = randint(10,100)
	height = randint(10,100)
	begin_fill()
	for repeats in range(2):
		forward(length)
		right(90)
		forward(height)
		right(90)
	end_fill()
	
def drawcircle():
	randomcolour()
	randomplace()
	hideturtle()
	diameter = randint(10,100)
	begin_fill()
	circle(diameter)
	end_fill()
	
def drawstar():
	randomcolour()
	randomplace()
	hideturtle()
	begin_fill()
	length = randint(10,100)
	for point in range(5):
		forward(length)
		left(144)
	end_fill()
	
##for i in range(60):
##	shape("turtle")
##	randomcolour()
##	randomplace()
##	randomheading()
##	stamp()
	
clear()
setheading(0)

for shape in range(40):
	drawrectangle()
	drawcircle()
	drawstar()
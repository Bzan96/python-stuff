# !python

import turtle as T
import random

# List of the positions of all star points
starList = []

'''
	Containing an algorithm that prevents two star points to overlap.
	No solution yet for preventing two stars from overlapping at all.
	Doubtful if it's even possible without declaring a collision object.
'''

def star():
	T.speed("fast")
	T.penup()
	newx = random.randrange(-675,675)
	newy = random.randrange(-375,375)
	T.setx(newx)
	T.sety(newy)
	T.pendown()
	T.color("yellow", "yellow")
	T.begin_fill()
	for i in range(5):
		starPos = T.pos()
		starList.append(starPos)
		T.forward(25)
		T.left(144)
	T.end_fill()
	
tempStarCount = 0

T.setup(width=1400, height=800, startx=0, starty=0)
		
T.bgcolor("black")
T.title("Starry sky")
for i in range(100):
	starPos = T.pos()
	if starPos in [starList]:
		pass
	else:
		star()
		tempStarCount += 1

T.penup()
T.exitonclick()

print(tempStarCount)
##starList.sort()
##print(starList)
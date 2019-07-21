from turtle import *
from random import randint

penup()
goto(-140,140)
speed(0)

for i in range(25):
	write(i, align="center")
	right(90)
	forward(10)
	for j in range(10):
		pendown()
		forward(7.5)
		penup()
		forward(7.5)
	backward(160)
	left(90)
	forward(20)

# Turtle One
t1 = Turtle()
t1.color("green")
t1.shape("turtle")

t1.penup()
t1.goto(-160,70)
t1.pendown()
	
# Turtle Two
t2 = Turtle()
t2.color("red")
t2.shape("turtle")

t2.penup()
t2.goto(-160,100)
t2.pendown()

# Turtle Three
t3 = Turtle()
t3.color("blue")
t3.shape("turtle")

t3.penup()
t3.goto(-160,40)
t3.pendown()

# Turtle Four
t4 = Turtle()
t4.color("yellow")
t4.shape("turtle")

t4.penup()
t4.goto(-160,10)
t4.pendown()

for spin in range(10):
	t1.right(36)
	t2.right(36)
	t3.right(36)
	t4.right(36)

for turn in range(150):
	t1.forward(randint(1,5) )
	t2.forward(randint(1,5) )
	t3.forward(randint(1,5) )
	t4.forward(randint(1,5) )
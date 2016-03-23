import turtle
import random

'''
This is a program that draw with turtles.
'''

# set window and background color
window = turtle.Screen()
window.bgcolor("white")

# function for drawing a square
def draw_square():
	
	# this is brad
	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("#08a16d")
	brad.speed(4)

	count = 0
	while count < 4:
		brad.forward(100)
		brad.right(90)
		count = count + 1

# function for drawing a circle
def draw_circle():

	# this is angie
	angie = turtle.Turtle()
	angie.shape("turtle")
	angie.color("#4e697b")
	angie.penup()
	angie.setposition(-40, -60)
	angie.pendown()
	angie.circle(100)

# function for drawing a triangle
def draw_triangle():

	# this is susan
	susan = turtle.Turtle()
	susan.shape("turtle")
	susan.color("#565656")
	susan.speed(2)

	susan.penup()
	susan.setposition(-40, 80)
	susan.pendown()

	# creates two triangles
	n = 0
	while n < 2:
		count = 0
		susan.pendown()
		while count < 3:
			susan.left(120)
			susan.forward(100)
			count = count + 1
		susan.penup()
		susan.setposition(random.randint(-200,200),random.randint(-200,200))
		n = n + 1

# initialise drawing program
draw_square()
draw_circle()
draw_triangle()

# close when clicking window
window.exitonclick()

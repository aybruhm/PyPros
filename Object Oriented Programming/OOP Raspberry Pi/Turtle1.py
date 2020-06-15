from turtle import Turtle
from random import randint

israel = Turtle()
victor = Turtle()
jake = Turtle()
peace = Turtle()

israel.color('red')
israel.shape('turtle')

victor.color('blue')
victor.shape('turtle')

jake.color('green')
jake.shape('turtle')

peace.color('orange')
peace.shape('turtle')

israel.penup()
israel.goto(-320, 70)
israel.pendown()

victor.penup()
victor.goto(-320, 40)
victor.pendown()

jake.penup()
jake.goto(-320, 10)
jake.pendown()

peace.penup()
peace.goto(-320, 100)
peace.pendown()

for movement in range(220):
	israel.forward(randint(1,5))
	victor.forward(randint(1,5))
	jake.forward(randint(1,5))
	peace.forward(randint(1,5))
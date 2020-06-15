import turtle

israel = turtle.Turtle()

def square():
    israel.forward(100)
    israel.right(90)
    israel.forward(100)
    israel.right(90)
    israel.forward(100)
    israel.right(90)
    israel.forward(100)
    israel.right(90)
    israel.forward(100)

square()
israel.backward(200)
square()
israel.left(100)

# If-else statement
man = 100
woman = 87.5

if man < woman:
	square()
else:
	israel.right(200)

# While loops
israel = 'happy'

while israel == 'sad':
	israel_turtle.forward(10)

# For loops
for count in range(4):
	square()
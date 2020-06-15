from shapes import Traingle, Rectangle, Oval, Paper

rect1 = Rectangle()
rect2 = Rectangle()

rect1.set_width(200)
rect1.set_height(100)
rect1.set_color("blue")

rect2.set_width(50)
rect2.set_height(150)
rect2.set_color("yellow")

rect1.draw()

Paper.display()
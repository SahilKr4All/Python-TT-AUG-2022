Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#loop - repetition
import turtle
turtle.Screen()
<turtle._Screen object at 0x0000014699855A20>
turtle.Pen()
<turtle.Turtle object at 0x0000014699857670>
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)

turtle.reset()
for i in range(4):
    turtle.forward(100)
    turtle.left(90)


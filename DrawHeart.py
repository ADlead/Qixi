import turtle
import math
heart = turtle.Screen()
heart.setworldcoordinates(-7, -7, 7, 7) # set size
alex = turtle.Turtle()
alex.color("purple")  # set color
alex.pensize(7)
alex.penup()
alex.speed(7)
walkStart = -1
walkEnd = 1
i = walkStart
j = walkEnd
while i <= 0 and j >= 0:
    y1 = math.sqrt(1 - i * i) + (i * i) ** (1/4.0)
    y2 = -math.sqrt(1 - i * i) + (i * i) ** (1/4.0)
    y3 = math.sqrt(1 - j * j) + (j * j) ** (1/4.0)
    y4 = -math.sqrt(1 - j * j) + (j * j) ** (1/4.0)
    alex.setx(i)
    alex.sety(y1)
    alex.dot()
    alex.sety(y2)
    alex.dot()
    alex.setx(j)
    alex.sety(y3)
    alex.dot()
    alex.sety(y4)
    alex.dot()
    # adjust density
    i += 0.07
    j -= 0.07
heart.exitonclick()

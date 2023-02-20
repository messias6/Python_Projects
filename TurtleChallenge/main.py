from turtle import Turtle, Screen
from random import randint

tim = Turtle()
screen = Screen()
screen.colormode(255)

for n in range(3, 11):
    tim.color(randint(0, 255),
              randint(0, 255),
              randint(0, 255))

    for _ in range(n):
        tim.forward(50)
        tim.left(360/n)










screen.exitonclick()
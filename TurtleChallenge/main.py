import turtle
import random

turtle.colormode(255)
# Turtle
tim = turtle.Turtle()
tim.width(2)
tim.speed("fastest")

for n in range(0,360,5):
    tim.color(random.randint(0, 255),
              random.randint(0, 255),
              random.randint(0, 255))
    tim.setheading(n)
    tim.circle(100)







screen = turtle.Screen()
screen.exitonclick()
import turtle
import random

turtle.colormode(255)
# Turtle
tim = turtle.Turtle()
tim.width(10)
tim.speed("fastest")

directions = [0, 90, 270, 360]

for _ in range(200):
    tim.color(random.randint(0, 255),
              random.randint(0, 255),
              random.randint(0, 255))

    tim.forward(10)
    tim.setheading(random.choice(directions))








screen = turtle.Screen()
screen.exitonclick()
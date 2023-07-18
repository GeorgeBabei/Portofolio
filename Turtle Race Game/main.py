import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race?')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
all_turtles = []
name = ''
y = -150
for color in colors:
    name = colors[colors.index(color)]
    name = Turtle(shape='turtle')
    name.color(color)
    name.penup()
    name.goto(x=-230, y=y)
    y += 60
    all_turtles.append(name)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 210:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! {winning_color} turtle is the winner!")
        random_dist = random.randint(0, 10)
        turtle.forward(random_dist)


screen.exitonclick()
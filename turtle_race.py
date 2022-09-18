from turtle import Turtle, Screen
from random import randint
screen = Screen()
screen.setup(width=500, height=400)
user_input = screen.textinput(title="Make your bet", prompt="Which turtle win the race? Select color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [100, 60, 20, -10, -50, -90]
all_turtle = []


for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-235, y=y_positions[turtle_index])
    new_turtle.color(colors[turtle_index])
    all_turtle.append(new_turtle)

is_race_on = False
if user_input:
    is_race_on = True
while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 210:
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_input:
                print(f"You've won! The {winning_turtle} turtle is the winning turtle!")
            else:
                print(f"You've lose! The {winning_turtle} turtle is the winning turtle!")
            is_race_on = False
        random_distance = randint(0, 10)
        turtle.forward(random_distance)




screen.exitonclick()

import random
from turtle import Turtle, Screen

screen = Screen()
is_race_on = False

screen.setup(width=500, height=500)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle do you want to bet on?")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x = -230, y = y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print("You have won!")
            else:
                print("Sorry! You lost!")
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)



screen.exitonclick()


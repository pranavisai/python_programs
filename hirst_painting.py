import random
import turtle

turtle.colormode(255)
tim = turtle.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

color_list = [(226, 231, 236), (58, 106, 148), (225, 200, 109), (134, 84, 58), (223, 139, 64), (196, 145, 171), (224, 234, 230), (234, 226, 203), (142, 179, 204), (139, 81, 105), (210, 91, 68), (188, 79, 118), (236, 224, 232), (66, 106, 90), (135, 182, 137), (132, 134, 74), (64, 156, 90), (48, 156, 193), (183, 192, 201), (7, 49, 90), (215, 176, 190), (20, 67, 119), (174, 203, 181), (142, 29, 41), (225, 175, 168), (113, 124, 149), (65, 52, 38), (155, 206, 217), (149, 28, 21), (39, 58, 52)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for i in range(1, number_of_dots+1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if i % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)



screen = turtle.Screen()
screen.exitonclick()

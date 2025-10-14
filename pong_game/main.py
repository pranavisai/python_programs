import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
pong_ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, key="Down")
screen.onkey(l_paddle.go_up,key="w")
screen.onkey(l_paddle.go_down,key="s")

game_is_on = True
while game_is_on:
    time.sleep(pong_ball.move_speed)
    screen.update()
    pong_ball.move()

    if pong_ball.ycor() > 280 or pong_ball.ycor() < -280:
        pong_ball.bounce_y()

    if pong_ball.distance(r_paddle) < 50 and pong_ball.xcor() > 320 or pong_ball.distance(l_paddle) < 50 and pong_ball.xcor() < -320:
        pong_ball.bounce_x()

    if pong_ball.xcor() > 380:
        pong_ball.reset()
        scoreboard.l_point()

    if pong_ball.xcor() < -380:
        pong_ball.reset()
        scoreboard.r_point()


screen.exitonclick()
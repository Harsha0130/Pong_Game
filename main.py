from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

scr = Screen()
scr.tracer(0)
scr.bgcolor("black")
scr.setup(width=800, height=600)
scr.title("Pong Game")

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


scr.listen()
scr.onkeypress(r_paddle.go_up, "Up")
scr.onkeypress(r_paddle.go_down, "Down")
scr.onkeypress(l_paddle.go_up, "w")
scr.onkeypress(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    scr.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # Needs to bounce
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect collision with R_paddle
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect collision with L_paddle
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

scr.exitonclick()

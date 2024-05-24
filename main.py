from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

scr = Screen()
scr.tracer(0)
scr.bgcolor("black")
scr.setup(width=800, height=600)
scr.title("Pong Game")

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()


scr.listen()
scr.onkey(r_paddle.go_up, "Up")
scr.onkey(r_paddle.go_down, "Down")
scr.onkey(l_paddle.go_up, "w")
scr.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    scr.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # Needs to bounce
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()


scr.exitonclick()

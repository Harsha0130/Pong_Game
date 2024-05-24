from turtle import Screen
from paddle import Paddle

scr = Screen()
scr.tracer(0)
scr.bgcolor("black")
scr.setup(width=800, height=600)
scr.title("Pong Game")

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

scr.listen()
scr.onkey(r_paddle.go_up, "Up")
scr.onkey(r_paddle.go_down, "Down")
scr.onkey(l_paddle.go_up, "w")
scr.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    scr.update()

scr.exitonclick()

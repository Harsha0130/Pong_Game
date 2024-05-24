from turtle import Screen, Turtle
import time

scr = Screen()
scr.tracer(0)
scr.bgcolor("black")
scr.setup(width=800, height=600)
scr.title("Pong Game")

paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(5, 1)
paddle.penup()
paddle.goto(350, 0)


def go_up():
    new_y = paddle.ycor() + 30
    paddle.goto(paddle.xcor(), new_y)


def go_down():
    new_y = paddle.ycor() - 30
    paddle.goto(paddle.xcor(), new_y)


scr.listen()
scr.onkey(go_up, "Up")
scr.onkey(go_down, "Down")


game_is_on = True
while game_is_on:
    scr.update()

scr.exitonclick()

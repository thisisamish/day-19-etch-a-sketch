import turtle
from turtle import Turtle, Screen

MOVE_PACES = 20

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(MOVE_PACES)


def move_backward():
    tim.backward(MOVE_PACES)


def move_right():
    tim.right(MOVE_PACES)


def move_left():
    tim.left(MOVE_PACES)


def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()

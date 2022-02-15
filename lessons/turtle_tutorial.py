"""How to use Turtle."""

from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()
leo.color(99, 204, 250)

leo.penup()
leo.goto(45, 60)
leo.pendown()

leo.pencolor("pink")
leo.fillcolor(32, 67, 93)
leo.color("green", "pink")

leo.speed(50)

leo.begin_fill()
i: int = 0
while i < 3:
    leo.forward(300)
    leo.left(120)
    i += 1
leo.end_fill()
leo.hideturtle()

bob: Turtle = Turtle()
bob.color(0, 0, 0)
bob.penup()
bob.goto(45, 60)
bob.pendown()
bob.speed(75)
j: int = 0
k: int = 0
side_length: float = 300
while j < 3:
    bob.forward(side_length)
    bob.left(120)
    j += 1
while k < 200:
    side_length = side_length * 0.97
    bob.forward(side_length)
    bob.left(121)
    k += 1

done()
"""A sunset scene from my hometown <3.

Broke down complex function horizon (lines 38-56) into simpler functions waves (lines 59-74) and water (lines 77-93).
Tried something fun by using semi-circles in functions clouds (line 36), waves (line 72), and sun (line 107).
Used a while loop to create the clouds using semi-circles.
"""

__author__ = "730490894"

from turtle import Turtle, colormode, done
colormode(255)


def main() -> None:
    """The entrypoint of my scene."""
    turtle: Turtle = Turtle()
    clouds(turtle, -300, 200, 0.0)
    clouds(turtle, 0, 200, 0.0)
    clouds(turtle, 300, 200, 0.0)
    horizon(turtle, -500, -30)
    sun(turtle, 70, -30)
    shore(turtle, -500, -230)
    done()


def clouds(turtle_one: Turtle, x: float, y: float, heading: float) -> None:
    turtle_one.penup()
    turtle_one.goto(x, y)
    turtle_one.setheading(heading)
    turtle_one.pendown()
    turtle_one.pencolor(237, 67, 26)
    turtle_one.fillcolor(224, 123, 107)
    turtle_one.speed(75)
    turtle_one.begin_fill()
    i: int = 0
    while i < 4:
        turtle_one.circle(40, 180)
        turtle_one.right(90)
        i += 1
    turtle_one.end_fill()


def horizon(turtle_two: Turtle, x: float, y: float) -> None:
    """See the line where the sky meets the sea! Calls on waves and water functions to draw water using rectangles and semi-circles."""
    turtle_two.penup()
    turtle_two.goto(x, y)
    turtle_two.setheading(0.0)
    turtle_two.pendown()
    turtle_two.pencolor(44, 80, 123)
    turtle_two.speed(75)
    turtle_two.forward(1020)
    i: int = 0
    height: float = -60
    while i < 4:
        waves(turtle_two, -500, height)
        height -= 30
        i += 1
    water(turtle_two, -500, -60)
    

def waves(turtle_two: Turtle, x: float, y: float) -> None:
    """Draws waves with semi-circles that will be called in horizon function."""
    turtle_two.penup()
    turtle_two.goto(x, y)
    turtle_two.setheading(270.0)
    turtle_two.pendown()
    turtle_two.pencolor(44, 80, 123)
    turtle_two.fillcolor(44, 80, 123)
    turtle_two.begin_fill()
    turtle_two.speed(75)
    i: int = 0
    while i < 17:
        turtle_two.circle(30, 180)
        turtle_two.right(180)
        i += 1
    turtle_two.end_fill()


def water(turtle_two: Turtle, x: float, y: float) -> None:
    """Fills in water color to be called in horizon using rectangle."""
    turtle_two.penup()
    turtle_two.goto(x, y)
    turtle_two.setheading(0.0)
    turtle_two.pendown()
    turtle_two.pencolor(44, 80, 123)
    turtle_two.speed(75)
    turtle_two.begin_fill()
    i: int = 0
    while i < 2:
        turtle_two.forward(1020)
        turtle_two.left(90)
        turtle_two.forward(30)
        turtle_two.left(90)
        i += 1
    turtle_two.end_fill()


def sun(turtle_three: Turtle, x: float, y: float) -> None:
    """Draws setting sun with semi circle."""
    turtle_three.penup()
    turtle_three.goto(x, y)
    turtle_three.setheading(90.0)
    turtle_three.pendown()
    turtle_three.pencolor(235, 89, 43)
    turtle_three.fillcolor(242, 67, 40)
    turtle_three.begin_fill()
    turtle_three.speed(75)
    turtle_three.circle(90, 180)
    turtle_three.end_fill()
    turtle_three.hideturtle()


def shore(turtle_four: Turtle, x: float, y: float) -> None:
    """Draws warm sand to play on with rectangle."""
    turtle_four.penup()
    turtle_four.goto(x, y)
    turtle_four.setheading(0.0)
    turtle_four.pendown()
    turtle_four.pencolor(247, 201, 101)
    turtle_four.fillcolor(247, 201, 101)
    turtle_four.begin_fill()
    turtle_four.speed(75)
    i: int = 0
    while i < 2:
        turtle_four.forward(1020)
        turtle_four.left(90)
        turtle_four.forward(50)
        turtle_four.left(90)
        i += 1
    turtle_four.end_fill()


if __name__ == "__main__":
    main()
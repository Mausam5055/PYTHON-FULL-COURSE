import turtle
import colorsys

# Setup screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Beautiful Turtle Animation")

# Create turtle
t = turtle.Turtle()
t.speed(0)  # Set the turtle's speed to maximum
t.width(2)
t.hideturtle()

# Number of shapes
n = 36

# Animation loop
for i in range(360):
    color = colorsys.hsv_to_rgb(i / n, 1.0, 1.0)
    t.color(color)
    
    t.begin_fill()
    for _ in range(2):
        t.circle(100, 90)
        t.circle(100, 90)
    t.end_fill()

    t.right(10)

# Finish drawing
turtle.done()

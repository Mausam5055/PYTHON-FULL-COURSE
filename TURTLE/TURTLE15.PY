import turtle
import colorsys

# Setup the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Complex Pattern with Turtle")

# Create the turtle
t = turtle.Turtle()
t.speed(0)
t.width(2)
t.hideturtle()

# Number of patterns
n = 36
hue = 0.0

# Pattern drawing loop
for i in range(180):
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.seth(i * 2)
    hue += 0.005
    color = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    t.color(color)
    
    t.begin_fill()
    for j in range(2):
        t.circle(200-i, 90)
        t.circle(200-i, 90)
    t.end_fill()

    t.right(10)

# Finish drawing
turtle.done()

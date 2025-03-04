import turtle
import colorsys

# Setup the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Intricate Turtle Animation")

# Create turtle
t = turtle.Turtle()
t.speed(0)
t.width(2)
t.hideturtle()

# Number of shapes
n = 36
hue = 0

# Animation loop
for i in range(180):
    color = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    t.color(color)
    t.circle(i * 0.8, 180)  # Draw a semicircle
    t.right(45)  # Rotate the turtle
    t.circle(i * 0.8, 180)  # Draw another semicircle
    t.right(45)
    hue += 1/n

# Finish drawing
turtle.done()

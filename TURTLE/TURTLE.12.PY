import turtle
import colorsys

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle
t = turtle.Turtle()
t.speed(0)
t.width(2)
t.hideturtle()

# Number of spirals
n = 36

# Loop to create the spiral animation
for i in range(360):
    color = colorsys.hsv_to_rgb(i / n, 1.0, 1.0)  # Get a color from the HSV color wheel
    t.color(color)
    t.forward(i * 3 / n + i)  # Move the turtle forward
    t.left(59)  # Turn the turtle left
    t.left(59)  # Turn the turtle left again
    t.left(59)  # Turn the turtle left again

# Finish the drawing
turtle.done()



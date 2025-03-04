import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle
fractal_turtle = turtle.Turtle()
fractal_turtle.speed(0)  # Fastest speed
fractal_turtle.hideturtle()

# Function to draw a filled triangle
def draw_triangle(turtle, size, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(3):
        turtle.forward(size)
        turtle.left(120)
    turtle.end_fill()

# Recursive function to draw the Sierpinski Triangle
def sierpinski(turtle, order, size):
    if order == 0:
        draw_triangle(turtle, size, "black")
    else:
        for _ in range(3):
            sierpinski(turtle, order - 1, size / 2)
            turtle.forward(size)
            turtle.left(120)

# Position the turtle
fractal_turtle.penup()
fractal_turtle.goto(-150, -130)
fractal_turtle.pendown()

# Draw the Sierpinski Triangle
sierpinski(fractal_turtle, 4, 300)

# Hide the turtle and complete the drawing
fractal_turtle.hideturtle()
turtle.done()

import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle
star_turtle = turtle.Turtle()
star_turtle.shape("turtle")
star_turtle.color("blue")
star_turtle.speed(2)

# Function to draw a star
def draw_star(size):
    for _ in range(5):
        star_turtle.forward(size)
        star_turtle.right(144)

# Draw multiple stars
for i in range(5):
    draw_star(100)
    star_turtle.right(72)  # Rotate to create a star pattern

# Hide the turtle and complete the drawing
star_turtle.hideturtle()
turtle.done()

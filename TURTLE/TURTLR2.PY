import turtle
import colorsys

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle
spiral_turtle = turtle.Turtle()
spiral_turtle.shape("turtle")
spiral_turtle.speed(0)  # Fastest speed

# Function to draw a colorful spiral
def draw_spiral():
    num_colors = 360
    for i in range(num_colors):
        # Set color based on the position in the loop
        color = colorsys.hsv_to_rgb(i / num_colors, 1.0, 1.0)
        spiral_turtle.pencolor(color)
        
        # Draw a segment of the spiral
        spiral_turtle.forward(i * 3 / num_colors + i)
        spiral_turtle.right(59)  # Angle to create the spiral effect

# Draw the spiral
draw_spiral()

# Hide the turtle and complete the drawing
spiral_turtle.hideturtle()
turtle.done()

import turtle
import colorsys
import time

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("I Love You Priyanka Animation")

# Create a turtle for drawing text
text_turtle = turtle.Turtle()
text_turtle.hideturtle()
text_turtle.penup()
text_turtle.color("white")
text_turtle.speed(0)

# Function to animate text
def animate_text(text):
    text_turtle.clear()
    
    # Move text across the screen
    for x in range(-300, 300, 10):
        text_turtle.clear()
        text_turtle.color(colorsys.hsv_to_rgb((x + 300) / 600, 1.0, 1.0))
        text_turtle.goto(x, 0)
        text_turtle.write(text, align="center", font=("Arial", 24, "bold"))
        time.sleep(0.05)

# Animate the text
animate_text("I Love You Priyanka")

# Keep the window open
turtle.done()

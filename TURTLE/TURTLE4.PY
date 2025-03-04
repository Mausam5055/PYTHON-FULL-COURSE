import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Tic Tac Toe")
screen.bgcolor("white")

# Create a turtle for drawing the board
board_turtle = turtle.Turtle()
board_turtle.speed(0)
board_turtle.hideturtle()
board_turtle.pensize(3)

# Draw the Tic-Tac-Toe board
def draw_board():
    # Vertical lines
    for x in [-100, 100]:
        board_turtle.penup()
        board_turtle.goto(x, 300)
        board_turtle.pendown()
        board_turtle.goto(x, -300)
    
    # Horizontal lines
    for y in [-100, 100]:
        board_turtle.penup()
        board_turtle.goto(-300, y)
        board_turtle.pendown()
        board_turtle.goto(300, y)

draw_board()

# Create a turtle for drawing Xs and Os
game_turtle = turtle.Turtle()
game_turtle.hideturtle()
game_turtle.speed(0)
game_turtle.pensize(2)

# Initialize the game state
board = [["" for _ in range(3)] for _ in range(3)]
current_player = "X"

# Function to draw X or O on the board
def draw_mark(x, y, mark):
    row = (300 - y) // 100
    col = (x + 300) // 100
    if mark == "X":
        game_turtle.penup()
        game_turtle.goto(x - 30, y + 30)
        game_turtle.pendown()
        game_turtle.write("X", font=("Arial", 48, "bold"))
    elif mark == "O":
        game_turtle.penup()
        game_turtle.goto(x - 30, y + 30)
        game_turtle.pendown()
        game_turtle.write("O", font=("Arial", 48, "bold"))

# Function to handle mouse clicks
def click_handler(x, y):
    global current_player
    if x < -150 or x > 150 or y < -150 or y > 150:
        return  # Click is outside the board
    
    row = (300 - y) // 100
    col = (x + 300) // 100
    
    if board[row][col] == "":
        board[row][col] = current_player
        draw_mark(x, y, current_player)
        # Switch player
        current_player = "O" if current_player == "X" else "X"

# Bind the click handler to mouse clicks
screen.onclick(click_handler)

# Keep the window open
turtle.mainloop()

import math

while True:
    try:
        number = float(input("Enter a number to calculate its square root (enter 999 to stop): "))
        
        if number == 999:
            print("Exiting the program.")
            break

        if number < 0:
            print("Cannot calculate the square root of a negative number. Try again.")
            continue
        
        square_root = math.sqrt(number)
        print(f"The square root of {number} is {square_root}")
    
    except ValueError:
        print("Invalid input! Please enter a valid number.")

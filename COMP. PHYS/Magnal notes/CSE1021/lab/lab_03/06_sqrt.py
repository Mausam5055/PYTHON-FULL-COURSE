import math
while True:
    user_input = input("Enter a number to find its square root (or type 'exit' to exit): ")
    
    if user_input.lower() == 'exit':
        print("Exiting the program.")
        break
    
    try:
        number = float(user_input)
        
        if number < 0:
            print("Square root is not defined for negative numbers. Please try again.")
            continue
        
        square_root = math.sqrt(number)
        print(f"The square root of {number} is {square_root}")
    
    except ValueError:
        print("Invalid input! Please enter a valid number or 'exit' to quit.")

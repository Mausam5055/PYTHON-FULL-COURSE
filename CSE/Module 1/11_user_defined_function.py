# 2. Function With Parameters and Without Return Value
# This function takes inputs (parameters) but doesn’t return anything.
# It only performs an action.

#example: 

def greet(name):  
    print("Hello, " + name + "!")  # Uses the input 'name'

greet("Mausam")  # Calls the function with "Mausam"

#  Parameter:
# 1.name is the parameter (input) of the function.
# It holds the value "Mausam" when the function is called.

# 2. Return Value:
# This function does not return anything, it just prints a message.
# In Python, if a function doesn’t use return, it automatically 
# returns None.

#Example 2: 
def oddeven(a): 
    
    if a % 2 == 0:
        print(a, "is Even")
    else:
        print(a, "is Odd")
        
a =int(input("Enter a number:")) # Take input outside the function
oddeven(a)       


# ❌ Bad Approach (Input Inside Function)
#
# def oddeven():
#     a = int(input("Enter a number: "))  # Input inside function
#     if a % 2 == 0:
#         return f"{a} is Even"
#     else:
#         return f"{a} is Odd"

# print(oddeven())  # This function is NOT reusable
# 🔴 Problem: This function always takes input from the user, so you cannot 
# call it with a predefined number in another program.
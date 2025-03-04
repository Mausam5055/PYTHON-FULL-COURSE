#         Types of User-Defined Functions in Python 
#                (With Simple Explanation):

# A user-defined function is a function that a programmer 
# creates to perform a specific task. These functions can be 
# classified into different types based on how they handle 
# inputs and outputs.

# 1. Function Without Parameters and Without Return Value:
# This function doesn’t take any input and doesn’t return 
# anything.It simply performs a task like printing a message.
#Exapmle 1: 

def greet(): #no paramter i.e no value inside = ()
    print("Hello, welcome!")  # Just prints a message


greet()  # Calls the function 
         #no return value means no "print" 

#  Output: Hello, welcome!

 #Example 2: 

def oddeven():
    if a % 2 == 0:
        print(a, "is Even")
    else:
        print(a, "is Odd")

a = int(input("Enter a number: "))  # Take input from the user
# Calling the function
oddeven()  #no return value means no "print" 

# When is It a Problem?
# If you want to Use the function for multiple numbers
# Store the result for later use
# Pass numbers programmatically (without user input)
# Then, taking input inside the function is bad practice because it reduces 
# flexibility.
#          Return vs Print:

# 1.return: When a function returns something, you can use 
# that value elsewhere. For example, 
# you can store it in a variable, use it in calculations, 
# or return it to another function.

# 2.print: Printing simply displays something to the 
# screen, but the value doesn't go anywhere else in the
#  program.

#Example with Return:

a = int(input("Enter The First Number: "))
b = int(input("Enter The Second Number: "))
def add_numbers(a, b):  #here a nad b are the parameters of the function that we defined below 
    return a + b  # This function returns the sum, which can be used later
         
c = add_numbers(a, b)  #   The value of the function is stored inside the  
                       #   variable " c" which can be used in future 
print(c)  # Prints the returned value

sub = c - 4 
print(sub)  # the stored value inside varibale c is now used again 

#Here, the function returns the sum (c), which is 
# stored in the c variable and printed later.

# Example with Print:

def greet():
    print("Hello, welcome!")  # This just prints a message

greet()  # It only prints the message, no value is returned

# Here, the function does not return anything, it only 
# prints the message directly when called.

# In Short:
# 1.Returning: Sends a value back to the place where the 
# function was called. You can use or store that value.
# 2.Printing: Only displays something to the screen, 
# but doesn't send anything back for future use.

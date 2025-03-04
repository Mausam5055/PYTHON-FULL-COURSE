# ------CHAPTER 8 – FUNCTIONS & RECURSIONS-------

# A function is a group of statements performing a specific task.
# When a program gets bigger in size and its complexity grows,  
# it gets difficult for a program to keep track on which piece 
# of code is doing what!
# A function can be reused by the programmer in a given program 
# any number of

# -----EXAMPLE AND SYNTAX OF A FUNCTION-----

# The syntax of a function looks as follows:
#       def func1():
#       print('hello')
# This function can be called any number of times,
# anywhere in the program.


# --FUNCTION CALL--

# Whenever we want to call a function, we put the name of - 
# the function followed by parentheses as follows:
#func1() # This is called function call.

a = int(input("Enter your number:" ))
b = int(input("Enter your number:" ))
c = int(input("Enter your number:" ))

average = (a+b+c)/3
print(average)

a = int(input("Enter your number:" ))
b = int(input("Enter your number:" ))
c = int(input("Enter your number:" ))

average = (a+b+c)/3
print(average)

# (we can take out the average of thrre numbers as shown above
#  but if we are to take the average of 50 numbers (say) we cant
#  o by the above method since it will be very lengthy so for
#  which we can do it by the help functions)


# in short whenever a codee becomes too long we use the concept
# of function to separte out a particular logic in the entire code
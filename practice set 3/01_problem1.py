# 1. Write a python program to display a user entered
# name followed by Good Afternoon using input () function.

name = input("Enter your name: ")
print(f"Good Afternoon, {name} ") 


# NOTES:
# In Python, an f-string (formatted string literal) is 
# a way to embed expressions inside string literals, using 
# curly braces {}. The f or F before the string indicates 
# that the string is an f-string. This allows for easy and 
# readable string formatting.

# Basic Example of an f-string:
# name = "Alice"
# age = 30
# # Using an f-string to format the string
# message = f"My name is {name} and I am {age} years old."
# print(message)

# Explanation:
# f"...": The f before the string tells Python that this is an
# f-string.{name}: The expression inside the curly braces 
# {} is replaced by the value of the variable name that we give.
# {age}: Similarly, the value of age is inserted into the 
# string where {age} is placed.

# Output:
# My name is Alice and I am 30 years old.

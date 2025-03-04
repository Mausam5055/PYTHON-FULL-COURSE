# In Python, a module is simply a file that contains Python code, which can define functions, classes, and variables. Modules allow you to organize and reuse code across multiple programs.

# Types of Modules in Python
# Built-in Modules: These are modules that come with Python by 
# default. They provide functionality like math operations, 
# file handling, etc. 
# For example:

# 1.math – Provides mathematical functions.
# 2.os – Allows interaction with the operating system.
# 3.random – Helps generate random numbers.

#Example : 

import math
print(math.sqrt(16))  # Output: 4.0


# User-defined Modules: These are modules that you create 
# yourself. You can save your Python code in a .py file and 
# then import it into other programs.

# Example: Suppose you have a file named Two_module.py:

 # Two_module.py ahas the below given code
#       def greet(name):
#             return f"Hello, {name}!"

# You can import and use it in another Python file:

# import Two_module
# print(Two_module.greet("Mausam"))  # Output: Hello, Mausam!


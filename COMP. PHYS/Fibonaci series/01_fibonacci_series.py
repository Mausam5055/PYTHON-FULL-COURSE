# The Fibonacci series is a sequence of numbers where each 
# number is the sum of the two preceding ones, starting from 0 
# and 1.

# Formula:
# F(n)=F(n−1)+F(n−2)

import numpy as np
n = int(input("Enter Number Of terms:"))
fib = np.zeros(n)  # Create an array of size 'n' initialized with zeros
if n > 0:
    fib[0] = 0  # First Fibonacci number in the array
if n > 1:
    fib[1] = 1  # Second Fibonacci number in the array
for n in range(2, n):  # Loop from index 2 to (n-1)
    fib[n] = fib[n - 1] + fib[n - 2]  # Sum of previous two numbers
print(fib)  # Print the final Fibonacci series

# What is np.zeros()?
# np.zeros() is a NumPy function that creates an array of a 
# specified size, filled with zeros.

# When to Use np.zeros()?
#1. Initialize arrays before filling them with values.
#2. Avoid using Python lists for large numerical computations 
# (NumPy is faster).
#3.Pre-allocate memory for efficiency in large computations.

# The Fibonacci series is a sequence of numbers where each 
# number is the sum of the two preceding ones, starting from 0 
# and 1.

# Formula:
# F(n)=F(n−1)+F(n−2)


n = int(input("enter the number of terms to be printed:"))

f1 = 0
f2 = 1

print("The fibonacci series for ", n , " terms are: ")
print(f1)
for i in range(n-1):
    print(f2)  # we put the print in loop so all the values are printed one after another 
    next_term = f1 + f2
    f1 = f2
    f2  = next_term

# What is np.zeros()?
# np.zeros() is a NumPy function that creates an array of a 
# specified size, filled with zeros.

# When to Use np.zeros()?
#1. Initialize arrays before filling them with values.
#2. Avoid using Python lists for large numerical computations 
# (NumPy is faster).
#3.Pre-allocate memory for efficiency in large computations.

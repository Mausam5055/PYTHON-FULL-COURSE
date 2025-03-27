a = int(input("Enter first number: "))  
b = int(input("Enter second number: "))

def gcd(a, b):
    gcd = 1
    for i in range(1, min(a, b) + 1):  
        if a % i == 0 and b % i == 0:
            gcd = i  
    return gcd  

  
print("GCD:", gcd(a, b))  


# Understanding the Code:
# The function gcd(a, b) finds the greatest number that divides 
# both a and b completely without leaving a remainder.

# Example: Find GCD of 12 and 18
# Let's take:

# a = 12
# b = 18
# Step-by-Step Execution:
# Loop from 1 to min(a, b)

# The smallest number among 12 and 18 is 12, so we loop from 1
#  to 12.Check for common divisors

# If i divides both a and b exactly (i.e., a % i == 0 and 
# b % i == 0), then i is a common divisor.
# We keep updating gcd with the largest common divisor.
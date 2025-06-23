# write a function to calculate factorial of a given number and 
# the function should have one argument and return factorial value

def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f

a = int(input("Enter a number: "))
print("Factorial:", factorial(a))


# write a function to calculate factorial of a given number and 
# the function should have one argument and return factorial value

def factorial(n):
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact

num = int(input("Enter a number: "))
print("Factorial:", factorial(num))


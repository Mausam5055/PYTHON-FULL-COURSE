
# weknow:
# factorial(0) = 1
# factorial(1) = 1
# factorial(2) = 2 X 1
# factorial(3) = 3 X 2 X 1
# factorial(4) = 4 X 3 X 2 X 1
# factorial(5) = 5 X 4 X 3 X 2 X 1

# similarly,
# factorial(n) = n X n-1 X......3 X 2 X 1

# similarly,
# factorial(n) = n * factorial(n-1)

def factorial(n):
    if (n==1 or n==0):
      return 1    #for n=1,0 factorial(n) gives 1
    return n*factorial(n-1)   #or else in other case n! = n*(n-1)!

n = int(input("Enter a Number:"))
print(f"The factorial of the number is:{factorial(n)}")#f string has to be used for this purpose




n = int(input("Enter the value of n: "))  # Taking user input

f1 = 0
f2 = 1

if n == 1:
    print("The 1st Fibonacci number is:", f1)
elif n == 2:
    print("The 2nd Fibonacci number is:", f2)
else:
    for i in range(n - 2):  # Loop runs n-2 times because we already have f1 and f2
        next_term = f1 + f2
        f1 = f2
        f2 = next_term

    print("The nth Fibonacci number is:", f2)


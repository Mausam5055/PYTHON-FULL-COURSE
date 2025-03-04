def recursive_fibonacci(n):
    if n <= 1:
        return n
    return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)

def print_fibonacci_series(n):
    if n <= 0:
        print("Invalid input. n must be greater than 0.")
        return
    print("Fibonacci Series (Recursive):")
    for i in range(n):
        print(recursive_fibonacci(i), end=" ")
    print()

print_fibonacci_series(5)
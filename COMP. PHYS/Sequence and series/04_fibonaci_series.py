# What is the Fibonacci Series?
# The Fibonacci series is a sequence of numbers where each term is the sum of the two preceding terms. The series starts with 0 and 1 by default.

# Mathematical Formula:
# F(n)=F(n−1)+F(n−2)

# where: 
# F(0)=0 (First term)
# F(1)=1 (Second term)
# F(n)=F(n−1)+F(n−2) (For ≥2 n ≥2)


n = int(input("Enter the number of terms: "))  # Get user input

first = 0  # First number in the series
second = 1  # Second number in the series

for _ in range(n - 2):  # Loop to print remaining terms
    next_number = first + second  # Add previous two numbers
    print(next_number, end=" ")  # Print the next number
    first, second = second, next_number  # Update values

print("Fibonacci Series:", first, second, end=" ")  # Print first two numbers


# Normally, print() adds a newline ("\n") at the end, so each print() statement 
# moves to a new line.By using end=" ", the print statement ensures that the next
#  output (from the loop) continues on the same line with a space separating them.
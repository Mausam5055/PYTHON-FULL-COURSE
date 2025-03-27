def prime_factors(n):
    i = 2  # Start with the smallest prime number (2)
    while n > 1:  # Continue until n becomes 1
        if n % i == 0:  # If 'i' divides 'n' completely
            print(i, end=" ")  # Print the prime factor
            n = n // i  # Divide 'n' by 'i' to remove that factor
        else:
            i = i + 1  # Move to the next number

# Example run
n = int(input("Enter a number: "))  
print("Prime Factors:", end=" ")
prime_factors(n)


# How It Works:
#1. Start with i = 2 (smallest prime number).
#2. Check if i divides n completely:
#3. If yes, print i, divide n by i, and continue checking.
#4. If no, move to the next number i + 1.
#5. Repeat until n becomes 1.
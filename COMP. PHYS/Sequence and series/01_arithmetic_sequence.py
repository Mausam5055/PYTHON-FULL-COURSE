#ARTITHMETIC PROGRESSION

# Taking user input
a1 = int(input("Enter the first term (a1): "))
d = int(input("Enter the common difference (d): "))
n = int(input("Enter the number of terms (n): "))

# Generating the arithmetic sequence
arithmetic_seq = [a1 + (i - 1) * d for i in range(1, n + 1)]

# Printing the sequence
print("Arithmetic Sequence:", arithmetic_seq)


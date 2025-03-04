#GEOMETRIC PROGRESSION

# Taking user input
a1 = int(input("Enter the first term (a1): "))
r = int(input("Enter the common ratio (r): "))
n = int(input("Enter the number of terms (n): "))

# Generating the geometric sequence
geometric_seq = [a1 * (r ** (i - 1)) for i in range(1, n + 1)]

# Printing the sequence
print("Geometric Sequence:", geometric_seq)



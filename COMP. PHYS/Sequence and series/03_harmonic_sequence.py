#GEOMETRIC PROGRESSION

# Taking user input
a1 = float(input("Enter the first term of the corresponding AP (a1): "))
d = float(input("Enter the common difference of the AP (d): "))
n = int(input("Enter the number of terms (n): "))

# Generating the harmonic sequence
harmonic_seq = [1 / (a1 + (i - 1) * d) for i in range(1, n + 1)]

# Printing the sequence
print("Harmonic Sequence:", harmonic_seq)


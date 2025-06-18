def arithmetic_sequence(a1, n, d):
    return (a1 + (i - 1) * d for i in range(1, n + 1))

def geometric_sequence(a1, n, r):
    return (a1 * (r ** (i - 1)) for i in range(1, n + 1))

def harmonic_sequence(a1, n, d):
    return (1 / (a1 + (i - 1) * d) for i in range(1, n + 1))

# Parameters
a1 = 4
n = 5
d = 2
r = 3

# Generating sequences
arithmetic = list(arithmetic_sequence(a1, n, d))
geometric = list(geometric_sequence(a1, n, r))
harmonic = list(harmonic_sequence(a1, n, d))

# Output
print("Arithmetic Sequence:", arithmetic)
print("Geometric Sequence:", geometric)      
print("Harmonic Sequence:", harmonic)

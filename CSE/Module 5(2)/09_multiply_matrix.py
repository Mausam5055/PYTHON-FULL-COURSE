# Input matrix dimensions
m = int(input("Enter rows for 1st matrix: "))
n = int(input("Enter columns for 1st matrix: "))
p = int(input("Enter rows for 2nd matrix: "))
q = int(input("Enter columns for 2nd matrix: "))

# Checking if multiplication is possible
if n != p:
    print("Multiplication not possible...")
else:
    # Initializing matrices
    a = [[0 for _ in range(n)] for _ in range(m)]  # 1st matrix/nested list
    b = [[0 for _ in range(q)] for _ in range(p)]  # 2nd matrix
    c = [[0 for _ in range(q)] for _ in range(m)]  # Resultant matrix

    # Input for 1st matrix
    print("Enter elements for 1st matrix:")
    for i in range(m):
        for j in range(n):
            a[i][j] = int(input(f"Element at position ({i+1},{j+1}): "))

    # Input for 2nd matrix
    print("Enter elements for 2nd matrix:")
    for i in range(p):
        for j in range(q):
            b[i][j] = int(input(f"Element at position ({i+1},{j+1}): "))

    # Matrix multiplication
    for i in range(m):
        for j in range(q):
            for k in range(n):
                c[i][j] += a[i][k] * b[k][j]

    # Printing 1st matrix
    print("\nFirst Matrix:")
    for row in a:
        for num in row:
            print(num, end=" ")
        print()

    # Printing 2nd matrix
    print("\nSecond Matrix:")
    for row in b:
        for num in row:
            print(num, end=" ")
        print()

    # Printing Resultant matrix
    print("\nResultant Matrix (Multiplication):")
    for row in c:
        for num in row:
            print(num, end=" ")
        print()


#         🤔 So... Why i+1 and not just i?
# Python uses 0-based indexing, meaning:

# The first row is i = 0

# The first column is j = 0

# But in real-world terms, when a person is entering values, it's more natural to think:

# "I'm entering value for row 1, column 1" — not row 0, column 0.

# 🎯 Purpose of i+1 and j+1:
# It makes the user experience clearer when you're asking for input.
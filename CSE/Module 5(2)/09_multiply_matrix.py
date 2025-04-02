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
    a = [[0 for _ in range(n)] for _ in range(m)]
    b = [[0 for _ in range(q)] for _ in range(p)]
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
        print(" ".join(map(str, row)))

    # Printing 2nd matrix
    print("\nSecond Matrix:")
    for row in b:
        print(" ".join(map(str, row)))

    # Printing Resultant matrix
    print("\nResultant Matrix (Multiplication):")
    for row in c:
        print(" ".join(map(str, row)))
# Function for which we want to find the root
def f(x):
    return x**2 - 4  # Root at x = 2 and x = -2

# Bisection method with a tolerance of 1e-6
def bisection_method(f, a, b, tol=1e-6, max_iter=1000):
    if f(a) * f(b) >= 0:
        print("The function must have opposite signs at a and b.")
        return None

    m = (a + b) / 2.0
    for i in range(max_iter):
        m = (a + b) / 2.0
        fm = f(m)

        # Stop if the function value at m is within tolerance
        if abs(fm) < tol:
            return m

        # Update the interval based on the sign of f(m)
        if f(a) * fm < 0:
            b = m
        else:
            a = m

    print("Maximum iterations reached without convergence.")
    return m

# Call the function
root = bisection_method(f, 1, 3, tol=1e-6)
print("Root is approximately:", root)

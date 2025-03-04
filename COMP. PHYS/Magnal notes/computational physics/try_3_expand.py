# Function for which we want to find the root
def f(x):
    return x**3 - 0.165*x**2 + 3.99 * 10**(-4)

# Bisection method with 3 iteration
def bisection_method(f, a, b, max_iter=3):
    if f(a) * f(b) >= 0:
        print("The function must have opposite signs at a and b.")
        return None

    m = (a + b) / 2.0
    for i in range(max_iter):
        m = (a + b) / 2.0
        fm = f(m)

        # Update the interval based on the sign of f(m)
        if f(a) * fm < 0:
            b = m
        else:
            a = m

    print("Maximum iterations reached without convergence.")
    return m

# Call the function
root = bisection_method(f, 0, 0.11)
print("Root is approximately:", root)

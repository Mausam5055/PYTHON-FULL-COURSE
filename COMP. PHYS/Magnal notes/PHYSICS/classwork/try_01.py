from sympy import symbols, Eq, solve

# Define variables
x, y = symbols('x y')   

# Define the equations
eq1 = Eq(2*x + 3*y, 6)    
eq2 = Eq(x - y, 1)

# Solve the system of equations
solutions = solve((eq1, eq2), (x, y))

# Print the solutions
print(solutions)

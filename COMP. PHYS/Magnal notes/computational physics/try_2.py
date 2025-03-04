import numpy as np
import matplotlib.pyplot as plt

# Create a grid of x and y values
x = np.linspace(-5, 5, 400)
y = np.linspace(-5, 5, 400)
X, Y = np.meshgrid(x, y)

# Calculate Z, avoiding division by zero
Z = (X + Y - 3) / (X**2 - 1)
Z[np.abs(X**2 - 1) < 1e-10] = np.nan  # Set values where denominator is zero to NaN

# Plotting
plt.figure(figsize=(10, 8))
plt.contourf(X, Y, Z, levels=50, cmap='viridis')
plt.colorbar(label='z-value')
plt.title(r'Plot of $z = \frac{x+y-3}{x^2-1}$')
plt.xlabel('x')
plt.ylabel('y')
plt.axvline(x=1, color='red', linestyle='--', label='x = 1 (undefined)')
plt.axvline(x=-1, color='blue', linestyle='--', label='x = -1 (undefined)')
plt.legend()
plt.grid()
plt.show()

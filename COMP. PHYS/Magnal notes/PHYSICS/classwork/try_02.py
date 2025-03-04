import numpy as np
import matplotlib.pyplot as plt

# Define the equations
def eq1(x):
    return (6 - 2*x) / 3

def eq2(x):
    return x - 1

# Generate x values
x_values = np.linspace(-10, 10, 400)

# Calculate the corresponding y values
y_values_eq1 = eq1(x_values)
y_values_eq2 = eq2(x_values)

# Plot the equations
plt.plot(x_values, y_values_eq1, label=r'$2x + 3y = 6$', color='blue')
plt.plot(x_values, y_values_eq2, label=r'$x - y = 1$', color='red')

# Mark the intersection point
# The intersection point for this system is (3, 2)
plt.plot(3, 2, 'go', label='Intersection (3, 2)')

# Add labels and a legend
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(True)
plt.legend()
plt.title('Graphical Solution of the System of Equations')

# Show the plot
plt.show()

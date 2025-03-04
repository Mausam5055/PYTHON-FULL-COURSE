import numpy as np
import matplotlib.pyplot as plt

# Define the range of t
t = np.linspace(0, 2 * np.pi, 1000)

# Parametric equations for the heart
x = 16 * np.sin(t)**3
y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)

# Plot the heart shape
plt.figure(figsize=(6, 6))
plt.plot(x, y, color="red", linewidth=2)
plt.title("Heart Shape", fontsize=16)
plt.axis("off")  # Turn off the axes for aesthetics
plt.axis("equal")  # Equal scaling to make the heart look proportionate
plt.show()

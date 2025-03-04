import numpy as np
import matplotlib.pyplot as plt


time_seconds = np.arange(0, 7201, 300) 

def x_position(t):
    return -0.31 * t**2 + 7.2 * t + 28

def y_position(t):
    return 0.22 * t**2 - 9.1 * t + 30

x_values = x_position(time_seconds)
y_values = y_position(time_seconds)


plt.figure(figsize=(8,6))
plt.plot(x_values, y_values, marker='o', linestyle='-', color='b', label='Rabbit Trajectory')
plt.title("Rabbit's Trajectory across the Parking Lot")
plt.xlabel("x (meters)")
plt.ylabel("y (meters)")
plt.grid(True)
plt.legend()
plt.show()

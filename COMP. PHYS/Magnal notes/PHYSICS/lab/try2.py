import numpy as np
import matplotlib.pyplot as plt

# Define the trajectories for both holes
def trajectory_second_hole(x):
    return 0.58 * x - 0.0064 * x**2

def trajectory_fourth_hole(x):
    return 2.75 * x - 0.0306 * x**2

# Create an array of x values from 0 to 90 meters with a regular interval
x_values = np.linspace(0, 90, 100)

# Calculate the corresponding y values for both holes
y_second_hole = trajectory_second_hole(x_values)
y_fourth_hole = trajectory_fourth_hole(x_values)

# Plotting the trajectories
plt.figure(figsize=(12, 6))

# Plot for the second hole
plt.subplot(1, 2, 1)
plt.plot(x_values, y_second_hole, label='Second Hole', color='b')
plt.title('Golf Ball Trajectory - Second Hole')
plt.xlabel('Distance (m)')
plt.ylabel('Height (m)')
plt.xlim(0, 90)
plt.ylim(0, max(y_second_hole) + 5)
plt.grid()
plt.legend()

# Plot for the fourth hole
plt.subplot(1, 2, 2)
plt.plot(x_values, y_fourth_hole, label='Fourth Hole', color='g')
plt.title('Golf Ball Trajectory - Fourth Hole')
plt.xlabel('Distance (m)')
plt.ylabel('Height (m)')
plt.xlim(0, 90)
plt.ylim(0, max(y_fourth_hole) + 5)
plt.grid()
plt.legend()

# Show the plots
plt.tight_layout()
plt.show()

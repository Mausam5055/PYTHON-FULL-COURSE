import numpy as np
import matplotlib.pyplot as plt

# Function to get velocity and acceleration
def shm_values(A, w, phi, t):
    v = A * w * np.cos(w * t + phi)
    a = -A * w**2 * np.sin(w * t + phi)
    return v, a

# Constants
A = 5            # Amplitude
w = 2 * np.pi    # Angular frequency (1 Hz)
phi = 0          # Phase angle

# Time values
t = np.linspace(0, 2, 100)

# Empty lists to store values
velocity = []
acceleration = []

# Calculate for each time
for ti in t:
    v, a = shm_values(A, w, phi, ti)
    velocity.append(v)
    acceleration.append(a)

# Plot
plt.plot(t, velocity, label="Velocity") #1st graph(t, velocity)
plt.plot(t, acceleration, label="Acceleration") #2nd graph(t, acceleration)
plt.title("SHM: Velocity and Acceleration")
plt.xlabel("Time (s)")
plt.ylabel("Value")
plt.show()

#write an algoritm to illustrate the motion of a simple 
# pendulum .The algorithm should take the reqd input and 
# simulate the motion

import numpy as np
import matplotlib.pyplot as plt

# === Inputs ===
L = float(input("Enter length of pendulum (m): "))
theta0_deg = float(input("Enter initial angle (degrees): "))
T = float(input("Enter total time to simulate (s): "))
dt = float(input("Enter time step (s): "))

# === Constants and Initialization ===
g = 9.81  # gravity
theta = np.radians(theta0_deg)  # convert to radians
omega = 0.0  # initial angular velocity
t = 0.0

# === Lists to store results ===
time_list = []
theta_list = []
x_list = []
y_list = []

# === Simulation loop (Euler's method) ===
while t <= T:
    alpha = - (g / L) * np.sin(theta)  # angular acceleration
    omega += alpha * dt
    theta += omega * dt

    # Save data
    time_list.append(t)
    theta_list.append(np.degrees(theta))  # store in degrees for readability
    x_list.append(L * np.sin(theta))
    y_list.append(-L * np.cos(theta))

    t += dt

# === Plot results ===
plt.figure(figsize=(10, 5))
plt.plot(time_list, theta_list)
plt.title("Simple Pendulum: Angular Displacement vs Time")
plt.xlabel("Time (s)")
plt.ylabel("Angle (degrees)")
plt.grid(True)
plt.show()

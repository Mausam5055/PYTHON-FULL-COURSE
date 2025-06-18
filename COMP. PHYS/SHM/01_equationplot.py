import numpy as np
import matplotlib.pyplot as plt

# Constants
A = 1.0                  # Amplitude
f = 1.0                  # Frequency in Hz
omega = 2 * np.pi * f    # Angular frequency
phi = 0                  # Phase

# Time array
t = np.linspace(0, 2, 1000)  # 0 to 2 seconds

# SHM Equations
x = A * np.cos(omega * t + phi)              # Displacement
v = -A * omega * np.sin(omega * t + phi)     # Velocity
a = -A * omega**2 * np.cos(omega * t + phi)  # Acceleration

# Plotting
plt.figure(figsize=(12, 6))

plt.plot(t, x, label='Displacement (x)', color='blue')
plt.plot(t, v, label='Velocity (v)', color='green')
plt.plot(t, a, label='Acceleration (a)', color='red')

plt.title('Simple Harmonic Motion: Displacement, Velocity, Acceleration')
plt.xlabel('Time (s)')
plt.ylabel('Value')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# show that for simple harmonic  motion the phase difference 
# betweeen : 1, displaement and velocity is pi/2 , vel and 
# aceeleration is pi/2 and displacement and acceleration in pi ,
# also write the code to graphically plot them":


import numpy as np
import matplotlib.pyplot as plt

# Parameters
A = 1             # Amplitude
omega = 2 * np.pi # Angular frequency (1 Hz)
t = np.linspace(0, 2, 1000)  # Time from 0 to 2 seconds

# SHM Equations
x = A * np.cos(omega * t)               # Displacement
v = -A * omega * np.sin(omega * t)      # Velocity
a = -A * omega**2 * np.cos(omega * t)   # Acceleration

# Plotting

plt.plot(t, x, label='Displacement', color='blue')
plt.plot(t, v, label='Velocity', color='green')
plt.plot(t, a, label='Acceleration', color='red')
plt.title('Simple Harmonic Motion: Phase Relationships')
plt.xlabel('Time (s)')
plt.ylabel('Magnitude')
plt.show()

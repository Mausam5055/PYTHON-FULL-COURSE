import numpy as np
import matplotlib.pyplot as plt

# Parameters
A = 1.0
f = 1.0
omega = 2 * np.pi * f

# Time values
t = np.linspace(0, 2, 1000)
dt = t[1] - t[0]

# Displacement
x = A * np.cos(omega * t)

# Velocity and Acceleration using gradient
v = np.gradient(x, dt)
a = np.gradient(v, dt)

# Plotting
plt.plot(t, x, label='Displacement', color='blue')
plt.plot(t, v, label='Velocity', color='green')
plt.plot(t, a, label='Acceleration', color='red')

plt.title('SHM: Displacement, Velocity, Acceleration')
plt.xlabel('Time (s)')
plt.ylabel('Value')
plt.legend()
plt.grid()
plt.show()

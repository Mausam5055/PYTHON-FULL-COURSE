import numpy as np
import matplotlib.pyplot as plt

m = 1.0 
g = 9.81 
h_max = 10.0  # maximum height (m)

# Generate heights (position) from 0 to h_max
heights = np.linspace(0, h_max, 100)

# Calculate velocities based on conservation of mechanical energy
# Total Energy (TE) at the maximum height is entirely potential energy.
TE = m * g * h_max  # Total Energy (constant)

# Compute Potential Energy (PE)
PE = m * g * heights

# Compute Kinetic Energy (KE)
KE = TE - PE  # Since TE = PE + KE, we can compute KE as TE - PE

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(heights, PE, label='Potential Energy (PE)', color='blue')
plt.plot(heights, KE, label='Kinetic Energy (KE)', color='red')
plt.plot(heights, TE * np.ones_like(heights), label='Total Energy (TE)', color='green', linestyle='--')

plt.title('Conservation of Energy: PE + KE = TE')
plt.xlabel('Height (m)')
plt.ylabel('Energy (Joules)')
plt.legend()
plt.grid(True)
plt.show()

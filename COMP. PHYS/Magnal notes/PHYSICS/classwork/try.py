import numpy as np
import matplotlib.pyplot as plt

# Given parameters
resistance = 10  # Resistance in ohms
voltage_range = np.arange(0, 20.5, 0.5)  # Voltage range from 0 to 20 V with 0.5 V step

# Calculate current using Ohm's Law: I = V / R
current = voltage_range / resistance

# Plotting the V vs I graph
plt.figure(figsize=(8, 6))
plt.plot(voltage_range, current, label="V vs I")
plt.title("V vs I Graph for a 10 Ω Resistor", fontsize=14)
plt.xlabel("Voltage (V)", fontsize=12)
plt.ylabel("Current (I) [A]", fontsize=12)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
# plt.axhline(0, color='black', linewidth=0.8)  # X-axis
# plt.axvline(0, color='black', linewidth=0.8)  # Y-axis
plt.legend()
plt.show()

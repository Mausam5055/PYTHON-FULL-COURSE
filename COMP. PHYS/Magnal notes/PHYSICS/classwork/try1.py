import numpy as np
import matplotlib.pyplot as plt

# Given parameters
resistances = [5, 20]  # Resistances in ohms
voltage_range = np.arange(0, 20.5, 0.5)  # Voltage range from 0 to 20 V with 0.5 V step

# Calculate currents for each resistance
current_5_ohm = voltage_range / resistances[0]  # Current for 5 Ω resistor
current_20_ohm = voltage_range / resistances[1]  # Current for 20 Ω resistor

# Plotting the V vs I graph
plt.figure(figsize=(8, 6))
plt.plot(voltage_range, current_5_ohm, label="5 Ω Resistor")
plt.plot(voltage_range, current_20_ohm, label="20 Ω Resistor")
plt.title("Comparative V vs I Graph for Resistors", fontsize=14)
plt.xlabel("Voltage (V)", fontsize=12)
plt.ylabel("Current (I) [A]", fontsize=12)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()

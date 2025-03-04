import matplotlib.pyplot as plt

# Data: Bond distances and electronic energies (in Hartrees)
bond_distances = [
    1.32, 1.42, 1.52, 1.62, 1.72, 1.82, 1.92, 2.02, 
    2.12, 2.22, 2.32, 2.42, 2.52, 2.62, 2.72
]
electronic_energies = [
    -198.8200, -198.8305, -198.8280, -198.8201, -198.8065,
    -198.7893, -198.7698, -198.7484, -198.7254, -198.7011,
    -198.6760, -198.6505, -198.6248, -198.5989, -198.5731
]

# Find the minimum energy
min_energy = min(electronic_energies)

# Calculate relative energies in kcal/mol
relative_energies = [(energy - min_energy) * 627.509 for energy in electronic_energies]

# Plotting
plt.figure(figsize=(8, 6))
plt.plot(bond_distances, relative_energies, marker='o', color='b', label='Relative Energy')
plt.title("Relative Energy vs. Bond Distance for F₂", fontsize=14)
plt.xlabel("Bond Distance (Å)", fontsize=12)
plt.ylabel("Relative Energy (kcal/mol)", fontsize=12)
plt.grid(alpha=0.3)
plt.legend(fontsize=10)
plt.tight_layout()
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Constants
hbar = 1.0545718e-34  # Reduced Planck's constant (J·s)
m = 9.10938356e-31    # Mass of the particle (electron mass in kg)
eV = 1.60218e-19      # Conversion factor from eV to J

# Simulation parameters
L = 2e-9              # Length of the domain (meters)
N = 2000              # Number of grid points
x = np.linspace(0, L, N)  # Position grid
dx = x[1] - x[0]         # Grid spacing
E = 0.5 * eV            # Particle energy (J)

# Define the potential for multiple barriers
def potential(x, barrier_positions, barrier_height, barrier_width):
    V = np.zeros_like(x)
    for pos in barrier_positions:
        V[(x > pos) & (x < pos + barrier_width)] = barrier_height
    return V

# Barrier parameters
barrier_positions = [0.5e-9, 1.0e-9, 1.5e-9]  # Positions of barriers (meters)
barrier_height = 1.0 * eV                     # Barrier height (J)
barrier_width = 0.1e-9                        # Barrier width (meters)

# Potential energy
V = potential(x, barrier_positions, barrier_height, barrier_width)

# Finite Difference Method: Solve Schrödinger Equation
def solve_schrodinger(V, E, dx, m, hbar):
    # Hamiltonian matrix construction
    diag = (2 * hbar**2 / (m * dx**2) + V)  # Diagonal terms
    off_diag = -hbar**2 / (2 * m * dx**2)   # Off-diagonal terms
    H = np.diag(diag) + np.diag(off_diag * np.ones(N-1), k=1) + np.diag(off_diag * np.ones(N-1), k=-1)
    
    # Solve eigenvalue problem for stationary states
    energies, wavefunctions = np.linalg.eigh(H)
    
    # Find the closest eigenstate to the input energy
    closest_idx = np.argmin(np.abs(energies - E))
    return energies[closest_idx], wavefunctions[:, closest_idx]

# Solve and get wavefunction for given energy
energy, wavefunction = solve_schrodinger(V, E, dx, m, hbar)

# Normalize the wavefunction
wavefunction = wavefunction / np.sqrt(np.sum(np.abs(wavefunction)**2) * dx)

# Transmission coefficient calculation
def transmission_probability(wavefunction, x):
    # Find the probability flux at the edges
    psi_in = wavefunction[:N//10]  # Region before the first barrier
    psi_out = wavefunction[-N//10:]  # Region after the last barrier
    P_in = np.sum(np.abs(psi_in)**2)
    P_out = np.sum(np.abs(psi_out)**2)
    return P_out / P_in  # Transmission probability

T = transmission_probability(wavefunction, x)

# Visualization
plt.figure(figsize=(12, 6))

# Plot potential energy
plt.plot(x * 1e9, V / eV, label="Potential Energy (eV)", color="black", linestyle="--")

# Plot wavefunction probability density
plt.plot(x * 1e9, np.abs(wavefunction)**2 * 1e3, label="Wavefunction Probability Density (x1000)", color="blue")

# Mark barrier regions
for pos in barrier_positions:
    plt.axvspan(pos * 1e9, (pos + barrier_width) * 1e9, color="gray", alpha=0.3, label="Barrier Region")

# Formatting
plt.title("Quantum Tunneling Through Multiple Barriers")
plt.xlabel("Position (nm)")
plt.ylabel("Energy (eV) / Probability Density")
plt.legend()
plt.grid()

# Display transmission probability
plt.text(1.5, max(V / eV) * 0.8, f"Transmission Probability: {T:.4f}", fontsize=12, color="red")
plt.show()

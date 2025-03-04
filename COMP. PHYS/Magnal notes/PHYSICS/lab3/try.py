# import numpy as np
# import matplotlib.pyplot as plt

# # Parameters
# A = 2
# w = np.sqrt(5)
# t = np.linspace(0, 10, 1000)

# # Phase angles in radians
# thetas = [0, np.radians(1), np.radians(2)]

# # Plotting Y(t), Velocity, and Acceleration
# plt.figure(figsize=(15, 10))

# # Plot Y(t)
# for theta in thetas:
#     Y = A * np.sin(w * t + theta)
#     plt.subplot(3, 1, 1)
#     plt.plot(t, Y, label=f'θ={np.degrees(theta)}°')

# plt.title('Position Y(t)')
# plt.xlabel('Time (s)')
# plt.ylabel('Y(t)')
# plt.legend()
# plt.grid()

# # Plot Velocity
# for theta in thetas:
#     v = A * w * np.cos(w * t + theta)
#     plt.subplot(3, 1, 2)
#     plt.plot(t, v, label=f'θ={np.degrees(theta)}°')

# plt.title('Velocity v(t)')
# plt.xlabel('Time (s)')
# plt.ylabel('v(t)')
# plt.legend()
# plt.grid()

# # Plot Acceleration
# for theta in thetas:
#     a = -A * w**2 * np.sin(w * t + theta)
#     plt.subplot(3, 1, 3)
#     plt.plot(t, a, label=f'θ={np.degrees(theta)}°')

# plt.title('Acceleration a(t)')
# plt.xlabel('Time (s)')
# plt.ylabel('a(t)')
# plt.legend()
# plt.grid()

# plt.tight_layout()
# plt.show()




import numpy as np
import matplotlib.pyplot as plt

# Given parameters
a_values = [0.1, 0.5, 0.9]  # 0 < a < 1
n_values = [1, 2, 3]
x = np.linspace(0, 1, 1000)  # 0 < x < a

# Create a figure and axis
fig, axs = plt.subplots(len(a_values), figsize=(8, 10))

# Loop over a values
for i, a in enumerate(a_values):
    # Loop over n values
    for n in n_values:
        y = np.sqrt(2) / a * np.sin(n * np.pi * x / a)
        axs[i].plot(x, y, label=f"n = {n}")

    axs[i].set_title(f"a = {a:.1f}")
    axs[i].set_xlabel("x")
    axs[i].set_ylabel("Y")
    axs[i].legend()
    axs[i].grid(True)

# plt.tight_layout()
plt.show()


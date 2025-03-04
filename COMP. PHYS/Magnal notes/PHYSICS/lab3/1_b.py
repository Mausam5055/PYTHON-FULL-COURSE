import numpy as np
import matplotlib.pyplot as plt
A = 2
w = np.sqrt(5)
t = np.linspace(0, 10, 10000)

thetas = [0, 1, 2]
thetas = [np.radians(theta) for theta in thetas]

for theta in thetas:
    v = A * w * np.cos(w * t + theta)
    plt.subplot(2, 1, 1)
    plt.plot(t, v, label=f'θ={np.degrees(theta)}°')

plt.title('Velocity v(t)')
plt.xlabel('Time (s)')
plt.ylabel('v(t)')
plt.legend()

for theta in thetas:
    a = -A * w**2 * np.sin(w * t + theta)
    plt.subplot(2, 1, 2)
    plt.plot(t, a, label=f'θ={np.degrees(theta)}°')

plt.title('Acceleration a(t)')
plt.xlabel('Time (s)')
plt.ylabel('a(t)')
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()
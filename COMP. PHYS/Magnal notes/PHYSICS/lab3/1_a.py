import numpy as np
import matplotlib.pyplot as plt
A = 2
w = np.sqrt(5)
t = np.linspace(0, 10, 10000)

thetas = [0, 1, 2]
thetas = [np.radians(theta) for theta in thetas]

plt.figure(figsize=(5, 5))

for theta in thetas:
    Y = A * np.sin(w * t + theta)
    plt.plot(t, Y, label=f'θ={np.degrees(theta)}°')

plt.title('Position Y(t)')
plt.xlabel('Time (s)')
plt.ylabel('Y(t)')
plt.legend()
plt.show()
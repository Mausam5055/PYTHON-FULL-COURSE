# from matplotlib import pyplot as plt

# x = list(range(0,100))
# y = list(map(lambda x : x*x , x ))

# print(y)

# plt.plot(x,y)
# plt.show()


import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
y4 = np.exp(-x)

# Create a figure with 2 rows and 2 columns of subplots
plt.subplot(2, 2, 1)  # Row 1, Column 1
plt.plot(x, y1, label='sin(x)')
plt.title('Sine Wave')

plt.subplot(2, 2, 2)  # Row 1, Column 2
plt.plot(x, y2, label='cos(x)', color='r')
plt.title('Cosine Wave')

plt.subplot(2, 2, 3)  # Row 2, Column 1
plt.plot(x, y3, label='tan(x)', color='g')
plt.ylim(-10, 10)  # Limit y-axis for tan(x) to avoid large values
plt.title('Tangent Wave')

plt.subplot(2, 2, 4)  # Row 2, Column 2
plt.plot(x, y4, label='exp(-x)', color='m')
plt.title('Exponential Decay')

# Display the plot
plt.tight_layout()  # Adjust layout to prevent overlapping
plt.show()

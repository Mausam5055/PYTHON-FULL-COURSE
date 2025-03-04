import matplotlib.pyplot as plt
import numpy as np

def y1(x):
    return 1/x

def y2(x):
    return x

x_values = np.linspace(0,50,10000)  #numpy.linspace(start, stop, num of points needed in between start and stop)

y1_values = y1(x_values)
y2_values = y2(x_values)

plt.plot(x_values, y1_values)
plt.plot(x_values, y2_values)

plt.show()
import matplotlib.pyplot as plt
import numpy as np
import math

x = [50,450,780,1200,4400,4800,5300]
y = [28,30,32,36,51,58,69]

p = np.pow(1,x)
y_fit = (28.32)*p

plt.scatter(x,y)
plt.plot(x,y_fit)

plt.xlabel('Altitude')
plt.ylabel('Dose of Radiaton')
plt.title('Plot 3')

plt.show()


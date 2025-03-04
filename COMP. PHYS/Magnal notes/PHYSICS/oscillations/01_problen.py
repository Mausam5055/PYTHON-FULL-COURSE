import numpy as np
import matplotlib.pyplot as plt

# def KE(x):
#     return 0.5*0.68*9.89

x = np.linspace(-0.11,0.11,1000)
ke = 0.5*0.68*9.89*9.89*((0.11*0.11) - (x*x))
pe = 0.5*65*(x*x)

plt.plot(x,ke)
plt.plot(x,pe)

plt.show()
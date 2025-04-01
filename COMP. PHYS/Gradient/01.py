import numpy as np
from matplotlib import pyplot as plt
x = [0,1,2,3,4,5,6,7,8,9]
y =[6,12,18,24,30,36,42,48,54,60]
z = np.gradient(x,y)
print(z)

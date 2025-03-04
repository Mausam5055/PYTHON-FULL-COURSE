import math as m
import numpy as np

A = [2, 4, -5]
B = [1, 2, 3]

AB = np.add(A,B)

sum = 0

for component in AB:
    sum += component**2


mag = m.sqrt(sum)

uv = AB/mag

print("The unit vector is : ",uv)


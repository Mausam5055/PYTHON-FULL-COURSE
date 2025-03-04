import math as m
import numpy as np

def phi(x,y,z):
    phi = 3*x*2*z - x*y*3 + 5
    return phi

list = [(0, 0, 0), (1, -2, 2), (-1, -2, -3)]

values= [0]*len(list)

for i in range(len(list)):
    x, y, z = list[i]
    values[i] = phi(x, y, z)  # Store the result directly


for i in range(len(list)):
    
    print(f"f({list[i]}) = {values[i]}")

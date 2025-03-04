import math as m
import numpy as np

A = [1+2*(3)**(0.5), 1, 2]
B = [1, 1, 2]
C = [1, 3, 2]

AB = np.subtract(A, B)
AC = np.subtract(A, C)


l = len(AB)
res = 0
a=0
b=0
for i in range(l):
 res += AB[i]*AC[i]
 a+= AB[i]*AB[i]
 b+= AC[i]**2

aa = m.sqrt(a)
bb = m.sqrt(b)

cos_theta = res/(aa*bb)
ang_rad = m.acos(cos_theta)
ang_deg = m.degrees(ang_rad)

print("The value of Angle is : ", ang_deg)

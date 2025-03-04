import math as m
import numpy as np

A = [1,2,3]
B = [2,4,5]

l = len(A)
res = 0
a=0
b=0
for i in range(l):
 res += A[i]*B[i]
 a+= A[i]*A[i]
 b+= B[i]**2

aa = m.sqrt(a)
bb = m.sqrt(b)
print("The Dot product is : ", res)

cos_theta = res/(aa*bb)
ang_rad = m.acos(cos_theta)
ang_deg = m.degrees(ang_rad)

print("The value of Angle is : ", ang_deg)

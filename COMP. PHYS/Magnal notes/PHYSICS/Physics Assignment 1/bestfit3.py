import matplotlib.pyplot as plt
import math
import numpy as np

x = [50,450,780,1200,4400,4800,5300]
y = [28,30,32,36,51,58,69]
n=len(x)
sumx = sum(x)
sumy = sum(np.log(y))

xy = 0
xx = 0

for i in range(n):
    xy += x[i]*math.log(y[i])
    xx += x[i]*x[i]

B = (sumx*sumy - n*xy)/(sumx*sumx - n*xx)
A = (sumy-B*sumx)/n

b = math.exp(B)
a = math.exp(A)

print(f'a = {a:.2f}')
print(f'b = {b:.2f}')
g = f'{b:.2f}^x'
print(f'The best fit straight line is y = {a:.2f}*{g}')
predicted_rad = a*math.pow(b,3000)
print(f'Predicted radiation dose at 3000 feet : {predicted_rad}')


print(sumx)
print(sumy)
print(xy)
print(xx)
print(B)
print(A)
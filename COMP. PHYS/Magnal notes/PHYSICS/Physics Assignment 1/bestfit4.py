import matplotlib.pyplot as plt
import math
import numpy as np

x = [350,400,50,600]
y = [61,26,7,2.6]
n=len(x)
sumx = sum(np.log(x))
sumy = sum(np.log(y))

xy = 0
xx = 0

for i in range(n):
    xy += math.log(x[i])*math.log(y[i])
    xx += math.log(x[i])*math.log(x[i])

b = (sumx*sumy - n*xy)/(sumx*sumx - n*xx)
A = (sumy-b*sumx)/n

a = math.exp(A)
print(b)

print(f'The best possible values for a and b are {a:.2f} and {b:.2f}')
b = f't^{b:.2f}'
print(f'The best fit straight line is v = {a:.2f}*{b}')


print(sumx)
print(sumy)
print(xy)
print(xx)

print(A)
print()
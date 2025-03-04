import matplotlib.pyplot as plt

x = [0,5,10,15,20,25]
y = [12,15,17,22,24,30]

n=len(x)
sumx = sum(x)
sumy = sum(y)

xy = 0
xx = 0

for i in range(n):
    xy += x[i]*y[i]
    xx += x[i]*x[i]

b = (sumx*sumy - n*xy)/(sumx*sumx - n*xx)
a = (sumy-b*sumx)/n

print(f'a = {a:.2f}')
print(f'b = {b:.2f}')
print(f'The best fit straight line is y = {a:.2f}+{b:.2f}*x')


print(sumx)
print(sumy)
print(xy)
print(xx)
import math

def fi(x):
    return math.pow(x,4)- x - 10

def fci(x):
    return 4*(math.pow(x,3))- 1

def calc_xn(x, f, fc):
    return x - (f/fc)

#to calculate range
# for i in range (0, 5):
#     if fi(i)*fi(i-1)<0:
#         x = i
x = 1
#main code
xn = calc_xn(x, fi(x), fci(x))

while abs(xn-x)>0.001 : 	#Can also use while xn!=x
    x = xn
    f = fi(x)
    fc = fci(x)
    xn = calc_xn(x, f, fc)
    # xn = round(xn,4)
    # x = round(x,4)

print(x)
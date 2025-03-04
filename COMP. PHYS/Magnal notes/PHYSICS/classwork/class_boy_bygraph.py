import matplotlib.pyplot as plt 
import numpy as np 
x1=0
x2=0
i=0
j=0
while i>=0:
    fx1=3-i-(2.72**(i-1))
    fx2=3-(i+1)-(2.72**((i+1)-1))
    fx3=3-j-(2.72**(j-1))
    fx4=3-(j-1)-(2.72**((j-1)-1))
    if ((fx1*fx2)<0):
        x1=i
        x2=i+1
        break
    elif ((fx1*fx2)==0):
        x1=i
        x2=i+2
        break
    elif ((fx3*fx4)<0):
        x1=j
        x2=j-1
        break
    elif ((fx1*fx2)<0):
        x1=j
        x2=j-2
        break 
    else:
        i+=1

x=np.linspace(x1,x2,10)
y1=2.72**(x-1)
y2=3-x

#fig = plt.figure(figsize = (10, 50))
plt.plot(x,y1)
plt.plot(x,y2)

plt.show()
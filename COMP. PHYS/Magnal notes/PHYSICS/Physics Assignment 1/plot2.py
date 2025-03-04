import matplotlib.pyplot as plt

x = [0,5,10,15,20,25]
y = [12,15,17,22,24,30]

fig = plt.figure(figsize = (4, 4))
plt.plot(x,y)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot 2')

plt.show()
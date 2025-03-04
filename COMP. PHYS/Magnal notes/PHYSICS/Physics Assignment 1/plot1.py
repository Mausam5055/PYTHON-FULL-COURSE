import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [16,19,23,26]

fig = plt.figure(figsize = (4, 4))
plt.plot(x, y)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot 1')


plt.show()
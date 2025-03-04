import matplotlib.pyplot as plt

x = [61,26,7,2.6]
y = [350,400,50,600]

fig = plt.figure(figsize = (4, 4))
plt.plot(x,y)

plt.xlabel('t(min)')
plt.ylabel('v(ft/min)')
plt.title('Plot 4')

plt.show()


import matplotlib.pyplot as plt

x = [50,450,780,1200,4400,4800,5300]
y = [28,30,32,36,51,58,69]

fig = plt.figure(figsize = (4, 4))
plt.plot(x,y)

plt.xlabel('Altitude')
plt.ylabel('Dose of Radiaton')
plt.title('Plot 3')

plt.show()


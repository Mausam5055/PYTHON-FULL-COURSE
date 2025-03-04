# importing the required module
from matplotlib import pyplot as plt
# x axis values
x = [1,2,3,4]
# corresponding y axis values
y = [16,19,23,26]
#giving title to my graph
plt.title("My first Graph")
#naming the axis 
plt.xlabel("x-Axis")
plt.ylabel("y-axis")

#plotiing the points
plt.plot(x,y)

#function to show the pot 
plt.show()
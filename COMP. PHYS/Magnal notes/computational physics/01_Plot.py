# importing the required module
from matplotlib import pyplot as p
# x axis values
x = [1,2,3,4]
# corresponding y axis values
y = [16,19,23,26]
# giving a title to my graph
p.title('My first graph!')

# plotting the points
p.plot(x, y)

# naming the x axis
p.xlabel('x - axis')
# naming the y axis
p.ylabel('y - axis')


# function to show the plot
p.show()
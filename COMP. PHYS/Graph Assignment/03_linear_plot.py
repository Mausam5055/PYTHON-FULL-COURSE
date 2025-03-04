#  3. Linear Plot
# Question: Plot a linear graph to visualize the change in temperature over a week. Use
#  the dataset:
# days = [’Monday’, ’Tuesday’, ’Wednesday’, ’Thursday’, ’Friday’, ’Saturday’, ’Sunday’]
#  temperatures = [22, 24, 21, 19, 23, 25, 20]
#  Expected Plot: A line plot with days on the x-axis and temperatures on the y-axis.

from matplotlib import pyplot as plt
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
temperatures = [22, 24, 21, 19, 23, 25, 20]
plt.title("Change In Temp Over Week")
plt.xlabel("days")
plt.ylabel("temperatures")
plt.plot(days,temperatures)
plt.show()

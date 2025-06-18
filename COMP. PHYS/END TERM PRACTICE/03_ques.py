import numpy as np
import matplotlib.pyplot as plt
u = 20
theta_degrees = 30
theta_radians = np.radians(theta_degrees)
g = 9.81

time_of_flight = (2 * u * np.sin(theta_radians)) / g
max_height = (u**2 * (np.sin(theta_radians)**2)) / (2 * g)  
range_of_projectile = (u**2 * np.sin(2 * theta_radians)) / g
print("Time of Flight:", time_of_flight)
print("Maximum Height:", max_height)
print("Range of Projectile:", range_of_projectile)

#plotting the trajectory

#Time Intervalas
t = np.linspace(0, time_of_flight, num=100)
#Calculating x and y coordinates(horizontal and vertical positions)
x = u * np.cos(theta_radians) * t # X = u * cos(theta) * t
y = u * np.sin(theta_radians) * t - 0.5 * g * t**2 # Y = u * sin(theta) * t - 0.5 * g * t^2


plt.plot(x, y)
plt.title("Projectile Motion")
plt.xlabel("Range ")
plt.ylabel("Height")
plt.show()
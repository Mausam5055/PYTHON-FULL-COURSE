import numpy as np
import matplotlib.pyplot as plt


x_values = np.linspace(0, 90, 500)  

def trajectory_second_hole(x):
    return 0.58 * x - 0.0064 * x**2

def trajectory_fourth_hole(x):
    return 2.75 * x - 0.0306 * x**2

y_second_hole = trajectory_second_hole(x_values)
y_fourth_hole = trajectory_fourth_hole(x_values)


plt.figure(figsize=(10, 6))
plt.plot(x_values, y_second_hole, label="Second Hole (30°)", color='g')
plt.plot(x_values, y_fourth_hole, label="Fourth Hole (70°)", color='r')
plt.title("Golf Ball Trajectories on the Second and Fourth Holes")
plt.xlabel("Horizontal Distance (m)")
plt.ylabel("Vertical Distance (m)")
plt.xlim(0, 90) 
plt.ylim(0, 60)  
plt.show()
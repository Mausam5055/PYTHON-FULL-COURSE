import numpy as np

time_minutes = np.arange(0, 121, 5)  
time_seconds = time_minutes * 60  

def x_position(t):
    return -0.31 * t**2 + 7.2 * t + 28

def y_position(t):
    return 0.22 * t**2 - 9.1 * t + 30

x_values = x_position(time_seconds)
y_values = y_position(time_seconds)

print("Time (min)\tX Position (m)\tY Position (m)")
for i in range(len(time_minutes)):
    min_time = time_minutes[i]
    x = x_values[i]
    y = y_values[i]
    print(f"{min_time}\t\t{x:.2f}\t\t{y:.2f}")

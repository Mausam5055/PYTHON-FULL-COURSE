import numpy as np
import matplotlib.pyplot as plt

h = np.linspace(0,20,20)
# v = np.linspace(20,0,20)
h_k = 20 - h

KE = 1*10*h_k
PE = 1*10*h
TE = KE + PE

plt.plot(h, TE, label = " Total Energy", color= "green" )
plt.plot(h, PE, label= "Potential Energy", color = "yellow") 
plt.plot(h, KE, label = "Kinetic Energy", color = "red")

plt.xlabel("Height", color = "blue")
plt.ylabel("Energy", color = "blue")
plt.title('Conservation of Energy: PE + KE = TE')
plt.legend()

plt.show() 
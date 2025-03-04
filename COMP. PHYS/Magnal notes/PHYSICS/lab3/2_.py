import numpy as np
import matplotlib.pyplot as plt

def Y(x, a, n):
    return (np.sqrt(2/a)* np.sin(n * np.pi * x / a))

a_values = np.linspace(0.1, 1, 3)  
n_values = [1, 2, 3] 
x_i = np.linspace(0, 1, 500) 
fig, axs = plt.subplots(len(a_values), figsize=(5, 5))

for i, a in enumerate(a_values):
    x = []
    Y_vals = []
    for n in n_values:
        for val_x in x_i:
            if val_x <= a:
                Y_vals.append(Y(val_x, a, n))
                x.append(val_x)

        l = len(Y_vals)
        axs[i].plot(x , Y_vals, label=f'a={a:.2f}, n={n}')

    axs[i].set_title(f"a = {a:.2f}")
    axs[i].set_xlabel('x')
    axs[i].set_ylabel('Y(x)')
    axs[i].legend()

plt.tight_layout()
plt.show()

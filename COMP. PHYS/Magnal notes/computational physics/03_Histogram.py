import matplotlib.pyplot as plt
# import numpy as np

bins = [65,70,75,80,85]
freq = [4,10,6,4]

plt.hist(bins[:-1], bins=bins, weights=freq, color='yellow', edgecolor='black')

plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Basic Histogram')

plt.show()
from matplotlib import pyplot as plt
categories = ['A', 'B', 'C', 'D', 'E']
values = [12,13,16,17,29]
plt.title("2nd Bar Garph")
plt.xlabel("Categories")
plt.ylabel("Value")
plt.bar(categories, values, color = "yellow")
plt.show()
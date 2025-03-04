# 8. Scatter Plot with Regression Line
# Question: Generate a scatter plot with a regression line to analyze the relationship
# between advertising spend and revenue. Use this dataset:
# ad_spend = [1000, 2000, 3000, 4000, 5000]
# revenue = [15000, 25000, 35000, 45000, 55000]
# Expected Plot: A scatter plot with ad spend on the x-axis and revenue on the
# y-axis, including a regression line.

from matplotlib import pyplot as plt
import numpy as np

ad_spend = [1000, 2000, 3000, 4000, 5000]
revenue = [15000, 25000, 35000, 45000, 55000]

plt.scatter(ad_spend, revenue)  # Scatter plot

m, b = np.polyfit(ad_spend, revenue, 1)  # Regression line
plt.plot(ad_spend, [m*x + b for x in ad_spend], color='red')

plt.xlabel('Ad Spend')
plt.ylabel('Revenue')
plt.show()

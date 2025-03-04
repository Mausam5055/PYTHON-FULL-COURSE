# 7. Linear Plot with Multiple Lines
# Question: Plot a line graph with two lines to compare the sales performance of two
# different products over a month. Use the following dataset:
# days = [’Week 1’, ’Week 2’, ’Week 3’, ’Week 4’]
# product_A_sales = [120, 135, 140, 150]
# product_B_sales = [100, 110, 120, 130]
# Expected Plot: A line plot with weeks on the x-axis and sales figures on the y-axis,
# showing two lines for Product A and Product B.

from matplotlib import pyplot as plt

days = ['Week 1', 'Week 2', 'Week 3', 'Week 4']
product_A_sales = [120, 135, 140, 150]
product_B_sales = [100, 110, 120, 130]
plt.xlabel('Weeks')
plt.ylabel('Sales')
plt.title('Sales Performance')

plt.plot(days, product_A_sales, label='Product A')
plt.plot(days, product_B_sales, label='Product B')

plt.legend()
plt.show()

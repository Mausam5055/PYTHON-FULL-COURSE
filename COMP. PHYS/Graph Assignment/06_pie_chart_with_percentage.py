# 6. Pie Chart with Percentages
# Question: Create a pie chart with percentages displayed on each slice. Use the dataset:
# categories = [’Electronics’, ’Furniture’, ’Groceries’, ’Clothing’]
# expenses = [400, 300, 500, 200]
# Expected Plot: A pie chart with each slice showing the percentage of total 
# expenses for each category

from matplotlib import pyplot as plt
# Pie Chart Data
categories = ['Electronics', 'Furniture', 'Groceries', 'Clothing']
expenses = [400, 300, 500, 200]
plt.title('Expense Distribution by Category')
plt.pie(expenses, labels=categories, autopct='%1.1f%%')
# Show plot
plt.show()
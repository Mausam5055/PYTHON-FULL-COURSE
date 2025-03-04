# 10. Pie Chart with Exploded Slices
# Question: Generate a pie chart with one exploded slice to emphasize the largest category.
# Use the following data:
# categories = [’Rent’, ’Utilities’, ’Groceries’, ’Entertainment’]
# expenses = [1200, 300, 400, 200]
# explode = (0.1, 0, 0, 0) % Explode the ’Rent’ slice
# Expected Plot: A pie chart with the ’Rent’ slice exploded to highlight it, showing
# the distribution of expenses.

from matplotlib import pyplot as plt

# Data
categories = ['Rent', 'Utilities', 'Groceries', 'Entertainment']
expenses = [1200, 300, 400, 200]
explode = (0.1, 0, 0, 0)  # Explode the 'Rent' slice

# Create pie chart
plt.pie(expenses, labels=categories, explode=explode, autopct='%1.1f%%', colors=['lightcoral', 'skyblue', 'lightgreen', 'gold'])

# Title
plt.title('Expense Distribution')

plt.show()


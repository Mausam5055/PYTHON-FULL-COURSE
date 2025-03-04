# 5. Bar Chart with Custom Colors
# Question: Plot a bar chart with custom colors for different product sales. 
# Use the dataset below:
# products = [’Product A’, ’Product B’, ’Product C’, ’Product D’]
# sales = [300, 150, 200, 250]
# colors = [’blue’, ’green’, ’red’, ’purple’]
# Expected Plot: A bar chart with each bar representing a product’s sales, 
# using the specified colors.

from matplotlib import pyplot as plt

# Data
products = ['Product A', 'Product B', 'Product C', 'Product D']
sales = [300, 150, 200, 250]
colors = ['blue', 'green', 'red', 'purple']

# Create bar chart
plt.bar(products, sales, color=colors)

# Labels and title
plt.xlabel('Products')
plt.ylabel('Sales')
plt.title('Product Sales with Custom Colors')

# Show plot
plt.show()

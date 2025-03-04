# What is a Pie Chart?
# A pie chart is a circular chart that represents data as slices of a pie, where 
# each slice corresponds to a proportion of the total.

# When to Use a Pie Chart?
# ✔️ To show percentage or proportional data.
# ✔️ To compare parts of a whole (e.g., market share, budget distribution).
# ✔️ When there are few categories (too many can make it cluttered).

import matplotlib.pyplot as plt

# Data
labels = ['Apple', 'Banana', 'Cherry', 'Grapes']
sizes = [30, 25, 20, 25]  # Percentage distribution
colors = ['red', 'yellow', 'pink', 'purple']  # Custom colors

# Add title
plt.title('Fruit Distribution')

# Create pie chart
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%' )


# Show plot
plt.show()

# notes : 
#1. autopct='%1.1f%%' → Displays percentages on the slices.
#2. startangle=140 → Rotates the chart for better visibility.
import matplotlib.pyplot as plt

# Data(list)
categories = ['A', 'B', 'C', 'D', 'E']
values = [10, 20, 15, 25, 30]


# Add labels and title
plt.title('Bar Graph Example')
plt.xlabel('Categories')
plt.ylabel('Values')

# Create bar plot
plt.bar(categories, values, color='black')

# Show plot
plt.show()


# NOTES: 
# 1.plt.bar() creates a bar graph.
# 2.categories represents the labels on the x-axis.
# 3.values represents the heights of the bars.
# 4.color='skyblue' sets the bar color.
# 5.plt.xlabel(), plt.ylabel(), and plt.title() add labels and a title.
# 6.plt.show() displays the graph.
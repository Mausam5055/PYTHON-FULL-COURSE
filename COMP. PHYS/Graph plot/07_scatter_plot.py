# What is a Scatter Plot?
# A scatter plot is a type of data visualization that shows the relationship 
# between two numerical variables. Each data point is represented as a dot on a 
# 2D plane.

# When to Use a Scatter Plot?
# 1.To identify correlations (e.g., height vs. weight).
# 2.To observe trends and patterns in data.
# 3.To detect outliers (unusual data points).

from matplotlib import pyplot as plt

# Sample data: X and Y values
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # X-axis values
y = [2, 4, 5, 7, 10, 11, 13, 15, 18, 20]  # Y-axis values


# Add labels and title
plt.xlabel('X-axis (Independent Variable)')
plt.ylabel('Y-axis (Dependent Variable)')
plt.title('Scatter Plot Example')

# Create scatter plot
plt.scatter(x, y, color='blue')

# Show plot
plt.show()

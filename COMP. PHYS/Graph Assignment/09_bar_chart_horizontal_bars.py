# 9. Bar Chart with Horizontal Bars
# Question: Create a horizontal bar chart to show the top 5 best-selling books in a store.
# Use the dataset:
# books = [’Book A’, ’Book B’, ’Book C’, ’Book D’, ’Book E’]
# copies_sold = [250, 300, 200, 400, 350]
# Expected Plot: A horizontal bar chart with books on the y-axis and copies sold on
# the x-axis

from matplotlib import pyplot as plt

books = ['Book A', 'Book B', 'Book C', 'Book D', 'Book E']
copies_sold = [250, 300, 200, 400, 350]

plt.barh(books, copies_sold)
plt.xlabel("Copies Sold")
plt.title("Top 5 Best-Selling Books")
plt.gca().invert_yaxis()
plt.show()

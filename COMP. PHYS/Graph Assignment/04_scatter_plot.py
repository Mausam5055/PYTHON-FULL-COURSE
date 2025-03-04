# 4. Scatter Plot
# Question: Create a scatter plot to show the relationship 
# between hours studied and
# scores obtained in an exam. Use the following dataset:
# hours_studied = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# scores_obtained = [55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
# Expected Plot: A scatter plot with hours studied on the x-axis 
# and scores obtained on the y-axis.

from matplotlib import pyplot as plt
hours_studied = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
scores_obtained = [55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
plt.scatter(hours_studied,scores_obtained , color='Yellow')
plt.title("Scatter Plot")
plt.xlabel("hours_studied")
plt.ylabel("scores_obtained")
plt.show()
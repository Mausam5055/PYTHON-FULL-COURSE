#             What is a Histogram?

# A histogram is a type of bar chart that represents the distribution of numerical 
# data. It divides the entire range of values into intervals (bins) and counts how
# many data points fall into each interval.

#             Key Features of a Histogram:

# 1.X-axis (Bins/Intervals): Represents ranges of data values.
# 2.Y-axis (Frequency): Represents the number of data points in each bin.
# 3.Bars Represent Data Distribution: Unlike a bar chart (which shows categories), 
# 4.a histogram shows continuous data distribution.

# Example: Understanding Histograms
# Imagine you have exam scores for 10 students:
# [50, 55, 60, 65, 70, 75, 80, 85, 90, 95]

# A histogram groups the scores into ranges (bins), such as:

# The values 50, 60, 70, 80, 90, and 100 define five bins:
# 50–60
# 60–70
# 70–80
# 80–90
# 90–100

# The histogram function groups the scores accordingly.
# So, a histogram would display 5 bars, each representing the count of students in 
# each range.


from matplotlib import pyplot as plt

# Sample exam scores
scores = [50, 55, 60, 65, 70, 75, 80, 85, 90, 95]

# Define bin edges explicitly
bins = [50, 60, 70, 80, 90, 100]  # Ensures correct range classification

plt.title('Histogram of Exam Scores')
plt.xlabel('Score Ranges')
plt.ylabel('Number of Students')

# Create the histogram
plt.hist(scores, bins=bins, color='skyblue', edgecolor='black', align='left')

# Add labels and title

# Show plot
plt.show()


# The histogram will have 5 bars.
# Each bar represents 2 students in a specific score range.
# The x-axis shows score ranges, and the y-axis shows the number of students.


# 1. Bar Chart
# Question: Create a bar chart that shows the number of students enrolled in different
# courses at a university. Use the following dataset:
# courses = [’Mathematics’, ’Physics’, ’Chemistry’, ’Biology’, ’Computer Science’]
# enrollment = [120, 85, 75, 90, 150]
# Expected Plot: A bar chart with courses on the x-axis and the 
# number of students on the y-axis.


from matplotlib import pyplot as plt
courses = ['Mathematics', 'Physics', 'Chemistry', 'Biology',' Computer Science']
enrollment = [120, 85, 75, 90, 150]
plt.title('Bar Graph')
plt.xlabel('courses')
plt.ylabel('enrollment')
plt.bar(courses, enrollment,color='red')
plt.show()
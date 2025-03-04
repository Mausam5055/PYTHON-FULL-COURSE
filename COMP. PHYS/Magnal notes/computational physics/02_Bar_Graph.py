import matplotlib.pyplot as plt

A = {'Batch 1':120, 'Batch 2':80, 'Batch 3':95,'Batch 4':100, 'batch 5': 60}

courses = list(A.keys())
values = list(A.values())

fig = plt.figure(figsize = (10, 5))

plt.bar(courses, values, color ='maroon',width = 0.4)

plt.xlabel("Batches")
plt.ylabel("No. of children")
plt.title("Students enrolled in different batches")
plt.show()
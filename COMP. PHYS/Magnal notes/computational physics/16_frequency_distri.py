import matplotlib.pyplot as plt
x = [20,15,5,20,20,15,15,15,10,10,10,20,15,5,18,18,18,18]
frequency={}
for item in x:
   if item in frequency:
      frequency[item] += 1
   else:
      frequency[item] = 1
print(frequency)
y = frequency.values()
x= frequency.keys()
plt.bar(x,y)
plt.xlabel("marks")
plt.ylabel("frequency")
plt.show()
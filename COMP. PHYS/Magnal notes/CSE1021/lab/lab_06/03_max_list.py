    # Using Built in function
list = [1,23,54,34,98]

max1 = max(list)
min1 = min(list)

print("The maximum element in the list(Built-in function): ",max1)
print("The minimum element in the list(Built-in function): ",min1)

# Using user defined function
max2 = float('-inf')    # max2 = min2 = list[0]
min2 = float("inf")
for i in list:
    if i>max2 :
        max2 = i
    if i < min2 :
        min2 = i
print("The maximum element in the list(User defined function): ",max2)
print("The minimum element in the list(User defined function): ",min2)
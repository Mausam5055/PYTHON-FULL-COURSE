list1 = [10, 20, 30, 40, 50, "VIT", 6, 7.8, "c"]
list1.append("a")  # Corrected: using list1 instead of list
list1.remove(20)    # Corrected: removing integer 20, not string "20"
print(list1)  # Output: [10, 30, 40, 50, 'VIT', 6, 7.8, 'c', 'a']

n = []
for i in range(1, 20):
    n.append(i)  # Appending numbers from 1 to 19
print(n)  # Output: [1, 2, 3, ..., 19]

# Correct way to remove all elements
n.clear()  # Instead of removing in a loop
print(n)  # Output: []

my_list=[1, 1, 2, 3, 3, "A", "A", "B", 9, 9, 10]
NewList=[]
for i in my_list:
    if i not in NewList:
        NewList.append(i)
print("The list with unique elements is: ", NewList)

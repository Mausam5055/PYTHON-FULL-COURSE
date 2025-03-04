# --------LIST COMPREHENSIONS--------

# List Comprehension is an elegant way to create lists based on 
# existing lists.
# list1 = [1,7,12,11,22,]
# list2 = [i for item in list 1 if item > 8]

myList = [1, 2, 9, 5, 3, 5]  #this is list one
squaredList = []             #this is list two

for item in myList:
    squaredList.append(item*item)

print(squaredList)

#in the second list we will get the ouput of the 1st list
#being multiplied with the number itself in the list

#but this same code can be written in a esay way using 
#"list comprehension" which will save our time as well
#wil reduce the lines of codes 

#see the next file for example
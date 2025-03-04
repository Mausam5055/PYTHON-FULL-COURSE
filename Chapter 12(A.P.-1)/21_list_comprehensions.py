myList = [1, 2, 9, 5, 3, 5]

# squaredList = []                 all these 3 lines are replaced by
# for item in myList:              a single line written below
#     squaredList.append(item*item)

squaredList = [i*i for i in myList]

print(squaredList)
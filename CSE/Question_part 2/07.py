n = input("enter any number:")
list1 = []
for i in n :
    if("0" <= i <= "9"):
        list1.append(i)

sorted_list = list(set(list1))
sorted_list.sort(reverse=True)
print(sorted_list[0])


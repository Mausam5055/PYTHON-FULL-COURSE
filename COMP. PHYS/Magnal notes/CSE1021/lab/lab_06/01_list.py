#1A
list_1 = [1, 2, 3, 4, 5]

#1B
list_2 = ["mangoes", "apples", "bananas", "Oranges"]

#1C
list_3 = ["Hii", 23, "apple", 69, "Paris", 6.9]

#1D
print(list_1)
list_1[1] = 7
print("Modify by index : ", list_1)

#1E
print(list_3)
list_3.append(77)
print(list_3)

#1F
list_3.insert(3,"Yousuf")
print(list_3)

#1G
print(list_3)
list_3.remove(69)
print(list_3)

#1H
list_2
pop = list_2.pop(1)
print(list_2)
print("Deleted element: ", pop )

#1I
print(list_2)
len = len(list_2)
print("length of created above : ", len)

#1J
print(list_3)
print("Is Paris in list: ", "Paris" in list_3)
print("Is London in list: ","London" in list_3)

#1K
print(list_2)
for members in list_2 :
    print(members)

#Concatenation of lists
    #using "+" operator
add_1 = list_1 + list_2
print("concatenated list is : ", add_1)

    #using append function
list_1.extend(list_2)  #you can also use "list_1.append(list_2)""
print("Using append:", list_1)

    #using user defined function
for i in list_2 :
    list_3.append(i)
print(list_3)


print(list_3.index(23))

list_1 = [1, 2, 3, 4, 5]
print(list_1.pop())
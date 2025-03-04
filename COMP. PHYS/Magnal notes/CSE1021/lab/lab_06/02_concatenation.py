#  USING '+' OPERATORS
list_1=[1,2,3,4,5,6]
list_2=[7,8,9,10]
list_3=list_1+list_2
print("USING '+' OPERATORS-",list_3)

#  USING BUILT-IN FUNCTION
list_1=[1,2,3,4,5,6]
list_2=[7,8,9,10]
list_1.extend(list_2)
print("USING BUILT-IN FUNCTION-",list_1)

#  WITHOUT USING BUILT-IN FUNCTION
list_1=[1,2,3,4,5,6]
list_2=[7,8,9,10]
list_3=[]
for i in list_1:
    list_3.append(i)
for i in list_2:
    list_3.append(i)
print("WITHOUT USING BUILT-IN FUNCTION-",list_3)

#  USING USER-DEFINED FUNCTION
def conList(list_1,list_2):
    list_3=list_1+list_2
    return list_3
list_1=[1,2,3,4,5,6]
list_2=[7,8,9,10]
NewList=conList(list_1,list_2)
print("USING USER-DEFINED FUNCTION-",NewList)

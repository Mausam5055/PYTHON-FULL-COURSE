# tuple can not be edited ones writen .....
tuple = (10,20,20,20,30,40)
print (tuple , end = " " )
print(type(tuple))
print (tuple.count(20))
print(tuple.index(20))
print(tuple[3:5])
print(tuple[0:5:2])
print(len(tuple))
print(max(tuple))
print(min(tuple))
print(sum(tuple))
print(any(tuple))
del tuple 
print (tuple)  # returns class....
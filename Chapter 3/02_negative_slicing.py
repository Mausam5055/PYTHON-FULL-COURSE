# Negative Indices: Negative indices can also be used as shown in the figure above. -1 
# corresponds to the (length - 1) index, -2 to (length - 2).


name = "Harry"

print(name[0:3])

print(name[-4: -1])
print(name[1:4])

print(name[:4]) # is same as print(name[0:4])
print(name[1:]) # is same as print(name[1:5])
print(name[1:5])



# note: the above is an alternative way to get the output without
# writing :
#         nameshort = name[0:3]  
#          print(nameshort)
#  which actually saves the time in writing the code
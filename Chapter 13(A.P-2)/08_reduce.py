# -------REDUCE EXAMPLE------

# Reduce applies a rolling computation to sequential pair of 
# elements.

# from functools import reduce
# val=reduce (function, list1) 

# # the function can be lambda function
# If the function computes sum of two numbers and the 
# list is [1,2,3,4]


from functools import reduce

l = [1, 2, 3, 4, 5]

def sum(a, b):
    return a + b

mul = lambda x,y:x*y

print(reduce(sum, l))
print(reduce(mul, l))

#the reduce function applies to operation to all the elements
#present in the list
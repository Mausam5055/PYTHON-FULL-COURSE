# --------MAP, FILTER & REDUCE-------

# Map applies a function to all the items in an 
# input_list.

# Syntax.
# map(function, input_list)
# # the function can be lambda function

     #map function example:

l = [1, 2, 3, 4, 5]

square = lambda x: x*x

sqList = map(square, l)
print(list(sqList))   #we wrote list so as to get the output 
                      #inform of list






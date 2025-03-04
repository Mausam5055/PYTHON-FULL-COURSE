#filter example:

# Filter creates a list of items for which the function 
# returns true.

# list(filter(function))
# # the function can be lambda function

l = [1, 2, 3, 4, 5]
def even(n):
    if(n%2 == 0):  #n%2 means remainder = 0
        return True
    return False   # we are already inside a def function
                   #so we dont have to write 'else'. 

onlyEven= filter(even, l)
print(list(onlyEven)) 
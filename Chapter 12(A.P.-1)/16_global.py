# -------THE GLOBAL KEYWORD----

# ‘global’ keyword is used to modify the variable outside of the current 
# scope.

a = 89

def fun(): 
    #global a
    a = 3
    print(a)


fun()
print(a)

#here a = 89 which is written outside the function is called a global
#variable
#now if write 'global a' inside the def fun() then our global variable
#will be changed from 89 to 3
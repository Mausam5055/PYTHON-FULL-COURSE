
# def square(a):
#     return a*a

# list = [1,2,3,4,5]
# list_sq = [square(i) for i in list]
# print(list_sq)

def finduc(s):
    snew = " "
    for i in s:
        if i not in snew:
            snew = snew + i 
    return snew
s = "programming"
print(finduc(s))

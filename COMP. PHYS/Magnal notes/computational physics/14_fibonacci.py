
n = int(input("No of terms: "))
term1 = 0
term2 = 1
mylist = []

mylist.append(term1)
for i in range(n):
    term3 = term1 + term2
    term1 = term2
    term2 = term3
    mylist.append(term1)

print(mylist)
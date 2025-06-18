

n = [[1,2,3],[4,5,6],[7,8,9]]
m = [[1,2,3],[4,5,6],[7,8,9]]
list3 = [[0,0,0],[0,0,0],[0,0,0]]

# adding two list 
for i in range(len(n)) :
    for j in range(len(n)) : 
        list3[i][j] = n[i][j]+m[i][j]

for i in range(len(n)) :
    for j in range(len(n)) : 
        print(list3[i][j],end = " ")
    print()
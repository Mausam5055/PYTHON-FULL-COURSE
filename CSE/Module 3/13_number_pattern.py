#write  a python code to print the following pattern:
#   1
#   2 2 
#   3 3 3
#   4 4 4 4
#HINT: this can be done by nested loops

row = 4
for i in range(1,row+1):
    for j in range(i):
        print(i, end = " ")
    print()  #move to the next lineafter printing a row 

#notes : here end=" " keeps printing on the same line with spaces 
#between each number
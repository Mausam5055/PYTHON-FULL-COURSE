#write  a python code to print the following pattern:
#   1
#   1 1 
#   1 1 1
#   1 1 1 1
#HINT: this can be done by nested loops

row = 4

for i in range(1,row+1):
    for j in range(i):
        print(1, end="")
    print()
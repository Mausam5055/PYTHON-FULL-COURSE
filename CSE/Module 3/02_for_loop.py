#compute the factorial using for loop

n = int(input("Enter The Number: "))
f = 1  # initialization
for i in range (1, n+1): # here i is the number of tiime the loop will exucute
    f = f*i

print("factorial=", f)

# in for  loop we fixed the range of the loop (i.e the number of time theloop
# will execute) from 1 to n+1 
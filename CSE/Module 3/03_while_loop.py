#compute the factorial of a number using whileloop:
num = int(input("Enter a number: "))
f = 1  # Initialize factorial as 1
i = 1  # Counter starts from 1

while i <= num:  #loop runs from 1<i<n times (here i is the loop number )
    f = f*i  # Multiply f by i(can also be written as : f*=i)
    i  = i+1  # loop Increase i by 1 and runs upto i/num times (can also be written as : i+=1 )

print("Factorial =", f)


# in while  loop we diddnt fixed the range of the loop (i.e the number of time theloop
# will execute) ratgher here the number of time the loop executes depends on the 
# other value
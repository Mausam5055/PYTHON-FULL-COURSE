# ----THE BREAK STATEMENT----

# ‘break’ is used to come out of the loop when encountered.
# It instructs the program to exit the loop now.


# ---THE CONTINUE STATEMENT---
# ‘continue’ is used to stop the current iteration of the loop and 
# continue with the next one. It instructs the Program to “skip this 
# iteration”.


for i in range(100):
    if(i == 34):
        break # Exit the loop right now(from 1 to 33 will be printed as we 
              #we put a break at 34 )
    print(i)

for i in range(100):
    if(i == 34):
        continue # Skip this iteration(1 to 100 will be printed except 34)
    print(i)    

#NOTES:1.BREAK FUNCTION IN LOOPS
#      2.CONTINUE FUNCTION IN LOOPS 
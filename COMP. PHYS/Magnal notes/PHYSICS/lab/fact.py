import math

l = int(input("Enter lower"))
u = int(input("Enter upper"))

for n in range(l,u+1):
    if n>1 :
       is_prime = True
    
    for i in range(2,n):
        if n%i==0:
            is_prime = False
    if is_prime :
          print(n)
          




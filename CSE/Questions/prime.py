prime = []
for i in range (2,101):
    is_prime = True 
    for j in range(2,int(i**0.5)+1):
        if j%i == 0:
         is_prime = False
         break
    if is_prime:
       prime.append(i)

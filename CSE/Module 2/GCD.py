a = int(input("Enter The First Number:"))
b = int(input("Enter The Seond Number"))
def GCD(a,b):
    while b:
     a,b = b, a%b 
    return a 

print("The GCD of ",a, "and",b ,"is", GCD(a,b))
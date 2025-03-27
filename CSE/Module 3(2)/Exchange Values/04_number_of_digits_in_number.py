n = int(input("Enter The Number :"))
s = 0
i = 0
while(n>0):
    d = n%10
    s = s+d
    n = n//10
    i += 1 
print(s)
print("Number Of Digits:", i)
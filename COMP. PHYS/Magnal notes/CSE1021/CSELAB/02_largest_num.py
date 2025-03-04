a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
c = int(input("Enter the third number : "))

if (a>b) :
    temp = a
    d = " The first number is biggest : "
else :
    temp = b
    d = "The second number is biggest : "
if temp<c :
    temp = c
    d = "The third number is biggest : "
print(d,temp)
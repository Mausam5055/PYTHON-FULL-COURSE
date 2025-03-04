n = 50
print("The even  Numbers Are : ")
for i in range(1,n+1):
    if i%2 == 0: 
        print(i)

n = 50
print("The even  Numbers Are : ")
for i in range(1,n+1):
    if i%2 != 0: 
        print(i)



n = int(input("Enter the number: "))
if n % 2 == 0:  # Use '==' for comparison
    print("The Number is Even")
else:
    print("The Number is Odd")


n = int(input("Enter the number: "))
if n % 2 != 0:  # If the remainder is not 0, it's an odd number
    print("The Number is Odd")
else:
    print("The Number Is Not Odd")



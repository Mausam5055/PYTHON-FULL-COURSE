#  USING MEMBERSHIP OPERATOR
print("Using Membership Operator")
my_list=[1,2,3,4,5,6,7,8,9,10]
element=int(input("Enter a number: "))
if element in my_list:
    print("The element is in the list")
else:
    print("The element is not in the list")

# WITHOUT USING MEMBERSHIP OPERATOR
print("Without Using Membership Operator")
my_list=[1,2,3,4,5,6,7,8,9,10]
element=int(input("Enter a number: "))
found = False
for i in my_list:
    if i==element:
        print("It is in the list")
        found = True
if not found:
    print("It is not in the list")

# IN CONTINUTION TO..... 05_super.py file......

# par kabhi kabhi hum cahte hy ki manager k constructor k saath 
# saath employee aur programmer ka constructor dono bhi run ho 
# tab hum kya karenge ......?

#matlab jab hum bhi hum manager ka constructor run kare tab manager
#ka constructor toh run ho paar uske saath saath baki upar wale 2 
#constructor bhi chale ....uske liye hum likhte hy
                                               # super().__int__()

#super class mean == parent class (here the parent class of manager is
#programmer)

class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a = 1 

class Programmer(Employee):
    def __init__(self):
        print("Constructor of Programmer")
    b = 2 

class Manager(Programmer):
    def __init__(self):
        print("Constructor of Manager")
    c = 3

# o = Employee()
# print(o.a) # Prints the a attribute 

o = Programmer()
print(o.a, o.b)


# o = Manager()
# print(o.a, o.b, o.c)
# ----------SUPER() METHOD------- 

# super() method is used to access the methods of a super
#  class in the  derived class.

# super().__init__()
# # __init__() Calls constructor of the base class

class Employee:
    def __init__(self):                #here we created a constructor     
        print("Constructor of Employee")
    a = 1 

class Programmer(Employee):
    def __init__(self):            #here we created a constructor
        print("Constructor of Programmer")
    b = 2 

class Manager(Programmer):
    def __init__(self):            #here we created a constructor
        print("Constructor of Manager")
    c = 3

o = Employee()               #o = object(here employee is the object)
print(o.a) # Prints the a attribute 

# o = Programmer()
# print(o.a, o.b)


# o = Manager()
# print(o.a, o.b, o.c)
 
#  ____NOTES___

#1. agar hum yeh upar wala code run karnge tab employee ka 
# constructor run hoga aur humko outupt 1 milega 
# (here object = employee)

# 2. agar hum: 
            # O = Employee
            # print(0.a) ko comment out karde aur fhir  
            #                                         # o = Programmer()
            #                                         # print(o.a, o.b) 
            #               ko run kare tab programmer ka constructor run hoga 
            #               aur humko output (1 2) milega
           

#3. similarly jab hum manager ka object banyenge tab manager ka constructor run hoga
     # o = Manager()          # manger ka object aise banta hy
     # print(o.a, o.b, o.c)  

    #  aur hum tab programmer aur employee wale object ko comment out kardenge
    #  uske baad humko output milega : (1 2 3)
 
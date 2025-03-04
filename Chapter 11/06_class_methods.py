# ----------CLASS METHOD-------

# A class method is a method which is bound to the class and not the object of the class.
# @classmethod decorator is used to create a class method.

# Syntax:
# @classmethod
# def(cls,p1,p2):

class Employee:
    a = 1
    
    def show(cls):
        print(f"The class value of a is {cls.a}")

e = Employee()
e.a = 45

e.show()


#here we will get the output as 45 if we run this above  code 
#(here,45 = class value)
#but if we want to get the output as 1 then we use the "class method"
#here (1 = class attribute) ----- see the next file
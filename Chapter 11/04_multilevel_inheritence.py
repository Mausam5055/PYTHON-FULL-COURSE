# -------MULTILEVEL INHERITANCE--------

# When a child class becomes a parent for another child class.
# (seee the pdf note for better understanding )

class Employee:
    a = 1 

class Programmer(Employee):
    b = 2 

class Manager(Programmer):
    c = 3

o = Employee()       #here 0 = object
print(o.a) # Prints the a attribute
# print(o.b) # Shows an error as there is no b attribute in Employee class

o = Programmer()
print(o.a, o.b)


o = Manager()
print(o.a, o.b, o.c)
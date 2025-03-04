# -------CHAPTER 11 - INHERITANCE & MORE ON OOPS------

# Inheritance is a way of creating a new class from an existing 
# class.
    
# Syntax:
# class Employee: # Base class 
# # Code
# class Programmer(Employee): # Derived or child class
# # Code


# We can use the method and attributes of ‘Employee’ in 
# ‘Programmer’ object.
# Also, we can overwrite or add new attributes and methods in 
# ‘Programmer’ class.

# ----------TYPES OF INHERITANCE-------
# • Single inheritance
# • Multiple inheritance
# • Multilevel inheritance

class Employee:
    company = "ITC"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")
        
class Programmer:
    company = "ITC Infotech"
    def show(self):
        print(f"the name is {self.name} and the salary is {self.salary}")
        
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language") 

a = Employee()
b = Programmer()          

print(a.company,b.company)


#in the same way as above we can create as many number of classes as 
# we want but for this purpose we have to write the same way for all
#other classes that we will create so to make this easy we take the help
#of inheritence as shown the next file


# -------CHAPTER 10 - OBJECT ORIENTED PROGRAMMING----------

# Solving a problem by creating object is one of the most popular approaches in 
# programming. This is called object-oriented programming.
# This concept focuses on using reusable code (DRY Principle). 


#    -----CLASS----
# A class is a blueprint for creating object.
# Syntax:
# class Employee: # Class name is written in pascal case
# # Methods & Variables 

# ----OBJECT-----
# An object is an instantiation of a class. When class is defined
# ,a template (info) is defined. Memory is allocated only after 
# object instantiation.Objects of a given class can invoke the 
# methods available to it without revealing the implementation 
# details to the user. Abstractions & Encapsulation!
 

#  eg of class as shown below:

class Employee:     #in this eg of class all the employes have name
    name = "Harry"  #harry and the language of all of them is py
    language = "Py"   #and their salary is 120000
    Salary = 120000


harry = Employee()  #here harry is an object
print(harry.name,harry.language, )    
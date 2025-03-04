class Employee: 
    language = "Python" # This is a class attribute(i.e by default
                        #its is set for all the employees working 
                        #under this class/company)
    salary = 1200000


harry = Employee()
harry.language = "JavaScript" # This is an instance attribute(
                            #means that it has been specifically
                            #added for a particular employee of the
                            #company/class)
print(harry.language, harry.salary)



# -------CLASS ATTRIBUTES----


# An attribute that belongs to the class rather than a particular object.
# Example:
# 39
# class Employee:
# company = "Google" # Specific to Each Class
# harry = Employee() # Object Instatiation
# harry.company
# Employee.company = "YouTube" # Changing Class Attribute


# ------INSTANCE ATTRIBUTES-----
# An attribute that belongs to the Instance (object). Assuming the class from the previous 
# example:
# harry.name = "harry"
# harry.salary = "30k" # Adding instance attribute 
# Note: Instance attributes, take preference over class attributes during assignment & 
# retrieval.

# When looking up for harry.attribute it checks for the following:
# 1) Is attribute present in object?
# 2) Is attribute present in class?
 
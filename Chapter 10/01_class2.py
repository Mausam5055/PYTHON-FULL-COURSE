class Employee:
     language = "Py"    #here the name of the employee is not assigned
     salary = 120000

harry = Employee()        #let the name of one employee be harry
print(harry.language,harry.salary)

rohan = Employee #let the name of another employee be rohan
print(rohan.salary,rohan.language)

# in the above: "class employee" means the class in which all the 
# Employees have a fixed salary of 12lakh and their language is py
# now when we specify the name of any employee and then we want 
# to get their salary and the language they use we use the help of 
# "OBJECT"  
#        i.e.   
#             harry = Employee()        #let the name of one employee be harry
#             print(harry.language,harry.salary)  #this is an object from a
                                                   #which is a part of class

# here harry (object) is one of the employee among all other employees
# who work in the company

#IN SHORT : CLASS: A COMPLETE COLECTION OF THE EMPLOYEES WORKING IN COMPANY
#            OBJECT: A SPECIFIC EMPLOYEE FROM THE COMPLETE COOLLECTION OF EMPLOYESES
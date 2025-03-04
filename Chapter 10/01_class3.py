#TO GIVE THE NAME OF ANY EMPLOYEE FROM THE CLASS OF EMPLOYEE:

class Employee:
     language = "Py"    #here the name of the employee is not assigned
     salary = 120000

harry = Employee()   
harry.name = "Harry singh"     #let the name of one employee be harry
print(harry.language,harry.salary,harry.name)

rohan = Employee
rohan.name = "Rohan kumar singh" #let the name of another employee be rohan
print(rohan.salary,rohan.language,rohan.name)

# Here name is instance attribute and salary and language are
#  class attributes as they directly belong to the class

# -----MODELLING A PROBLEM IN OOPS-----

# We identify the following in our problem.
# • Noun → Class → Employee
# • Adjective → Attributes → name, age, salary
# • Verbs → Methods → getSalary(), increment()
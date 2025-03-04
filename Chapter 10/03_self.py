# -----SELF PARAMETER ---- 

# self refers to the instance of the class. It is automatically passed
#  with a function call from an object.

# harry.getSalary() # here self is harry 
# # equivalent to Employee.getSalary(harry)

# The function getSalary() is defined as:
# class Employee:
# company = "Google"
# def getSalary(self):
# print("Salary is not there")

class Employee: 
    language = "Python" # This is a class attribute
    salary = 1200000

    def getInfo(self):     #inside bracket always we have to write self
        print(f"The language is {self.language}. The salary is {self.salary}")
#(inside class we used "getInfo" function)


harry = Employee()
harry.language = "JavaScript" 
Employee.getInfo(harry)
# harry.getInfo()      #this line can be written instead of above line
                        # (both are correct)   

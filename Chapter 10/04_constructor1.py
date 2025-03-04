# ------------__INIT__() CONSTRUCTOR--------

# __init__() is a special method which is first run as soon as the 
# object is created.
# __init__() method is also known as constructor.
# It takes ‘self’ argument and can also take further arguments.

# For Example:
            # class Employee:
            # def __init__(self, name):
            # self.name=name
            # def getSalary(self):
            # ...
            # harry = Employee("Harry")

class Employee: 
    language = "Python" # This is a class attribute
    salary = 1200000

    def __init__(self, name, salary, language): # dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")
 
 
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")


harry = Employee("Harry", 1300000, "JavaScript") 
# harry.name = "Harry"
print(harry.name, harry.salary, harry.language)

mausam = Employee("mausam",120000,"python")
print(mausam.name,mausam.salary,mausam.language)


#and here we can add as many empoyee as we want to...

#instead of giving harry.name = harry we created a function named as
#init function

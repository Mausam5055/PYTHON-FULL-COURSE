#instead of giving 'harry.name = harry' we created a function named as
#__init__ function to make our work easy

class Employee: 
    language = "Python" # This is a class attribute
    salary = 1200000

    def __init__(self,): # dunder method which is automatically called(undesroce start and underscore end words are called dunder method)
        print("I am creating an object")
 
 
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")


harry = Employee() 
harry.name = "Harry"
print(harry.name, harry.salary,)


#whenever we create a new object inside the calass, the dunder method 
# is called.eg. if we make a new object as "rohan = Employee" then the 
#word "i am creating a project is atomatically printed" after it

rohan = Employee()


mausam = Employee()

#and this continues as long as we kepp creating new objects
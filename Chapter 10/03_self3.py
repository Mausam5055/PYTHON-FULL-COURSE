# --------STATIC METHOD-------

# Sometimes we need a function that does not use the self-parameter.
# We can define a static method like this:
# @staticmethod # decorator to mark greet as a static method 
# def greet():
# print("Hello user")


class Employee: 
    language = "Python" # This is a class attribute
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():      #instead of self we wrote @static method above this line
        print("Good morning")


harry = Employee()
# harry.language = "JavaScript" # This is an instance attribute
harry.greet()
harry.getInfo() 
# Employee.getInfo(harry)
 



# We can put functions inside class (like: getinfo function,
# greet function and so on)

class Employee:
    language = "Python"
    salary = 120000

    def getInfo(self):
        print(f"The language is{self.language}.The salary is{self.salary}")

    def greet(self):
        print("Good morning")

harry = Employee()
harry.greet()
harry.getInfo()           
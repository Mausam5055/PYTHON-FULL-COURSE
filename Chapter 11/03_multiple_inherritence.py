# ----------MULTIPLE INHERITANCE---------

# Multiple Inheritance occurs when the child class inherits from more than one parent 
# classes.(see notes for better understanding)


class Employee:
    company = "ITC"
    name = "Default name"
    def show(self):
        print(f"The name of the Employee is {self.name} and the company is {self.company}")

class Coder:
    language = "Python"
    def printLanguages(self):
        print(f"Out of all the languages here is your language: {self.language}")
     


class Programmer(Employee, Coder): #we imported the "def show(self)" function and "def print(language)"
    company = "ITC Infotech"       #from the above two classes: 1.class employee and 2. class coder
    def showLanguage(self):
        print(f"The name is {self.company} and he is good with {self.language} language")


a = Employee()
b = Programmer()

b.show()
b.printLanguages()
b.showLanguage()
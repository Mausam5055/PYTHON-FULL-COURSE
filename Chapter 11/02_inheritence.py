#in the same way as above we can create as many number of classes as 
# we want but for this purpose we have to write the same way for all
#other classes that we will create so to make this easy we take the help
#of inheritence as shown below

# ----------SINGLE INHERITANCE----------
# Single inheritance occurs when child class inherits only a single parent class.


class Employee:
    company = "ITC"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

class Programmer(Employee):   #means, here programmer is a different class and 
                              #that we inherited from another class named "employee"
                              #this makes our way more easy and saves our time


    company = "ITC Infotech"            #the lines of codes here has decreasd
    def showLanguage(self):              #as compared to the previous code since we imported 'show(self') from above)
        print(f"The name is {self.name} and the salary is {self.language} language")

a = Employee()
b = Programmer()

print(a.company, b.company)




  

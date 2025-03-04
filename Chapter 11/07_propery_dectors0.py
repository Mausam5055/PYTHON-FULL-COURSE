#         ------@PROPERTY DECORATORS-------

# Consider the following class:
                                # class Employee:
                                # @property
                                # def name(self):
                                # return self.ename

# If e = Employee() is an object of class employee, 
# we can print (e.name) to print the
# ename by internally calling name() function.

#        ---- @.GETTERS AND @.SETTERS-----
# The method name with ‘@property’ decorator is called getter 
# method. We can define a function + @ name.setter decorator like 
# below:
            # @name.setter
            # def name (self,value):
            # self.ename = value

class Employee:
    a = 1
    
    def show(cls):
        print(f"The class value of a is {cls.a}")

        @property
        def name(self):
            self.ename

        @name.setter
        def name(self,value):
            self.ename = value    

e = Employee()
e.a = 45

e.name = "Harry Khan"
print(e.name)

e.show()

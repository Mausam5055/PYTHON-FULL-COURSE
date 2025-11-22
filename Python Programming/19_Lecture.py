# Problem 1: Employee and Engineer Class
# Requirement:
# Employee Class: Attributes (role, department, salary) and a method showDetails().
# Engineer Class: Inherits from Employee and adds name and age.

# Parent Class
class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary


    def showDetails(self):
        print(f"Role: {self.role}")
        print(f"Department: {self.department}")
        print(f"Salary: {self.salary}")

# Child Class (Inherits from Employee)
class Engineer(Employee):
    def __init__(self, name, age, role, department, salary):
        # Initialize the parent attributes
        super().__init__(role, department, salary)
        # Initialize the new attributes
        self.name = name
        self.age = age

    def showEngineerDetails(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        # Call the parent method to show the rest
        self.showDetails()

# --- Testing the Code ---
print("--- Problem 1 Output ---")
eng = Engineer("Alice", 28, "Software Dev", "IT", 85000)
eng.showEngineerDetails()



# Problem 2: Types of Inheritance
# Requirement: Show Multilevel, Multiple, and Hierarchical inheritance using specific vehicle classes.
# Hierarchical: One parent (Vehicle) has multiple children (Car, Motorcycle).
# Multilevel: Grandparent (Vehicle) -> Parent (Car) -> Child (SportsCars).
# Multiple: One child (LamborghiniCars) inherits from two parents (SportsCars, LuxuryMixin - Note: Since "Luxury" 
# wasn't in your list, I arranged the given classes to demonstrate the syntax purely.)

# Base Class
class Vehicle:
    def info(self):
        print("I am a generic Vehicle.")

# --- HIERARCHICAL INHERITANCE ---
# (Car and Motorcycle both inherit from Vehicle)
class Car(Vehicle):
    def car_info(self):
        print("I am a Car.")

class Motorcycle(Vehicle):
    def moto_info(self):
        print("I am a Motorcycle.")

# --- MULTILEVEL INHERITANCE ---
# (Vehicle -> Car -> SportsCars)
class SportsCars(Car):
    def sports_info(self):
        print("I am a fast Sports Car.")

# --- MULTIPLE INHERITANCE ---
# (Inheriting from two classes at once. 
# For this example, let's assume Ferrari inherits features of a SportsCar and a general Car directly)
class FerrariCars(SportsCars, Car):
    def ferrari_info(self):
        print("I am a Ferrari.")

class LamborghiniCars(SportsCars):
    def lambo_info(self):
        print("I am a Lamborghini.")

# --- Testing the Code ---
print("\n--- Problem 2 Output ---")
my_lambo = LamborghiniCars()
my_lambo.info()        # From Grandparent (Vehicle)
my_lambo.car_info()    # From Parent (Car)
my_lambo.sports_info() # From Parent (SportsCar)
my_lambo.lambo_info()  # From Self



# Problem 3: Using super()
# Requirement:
# Parent: Employee (name, salary).
# Child: SalesOfficer (inherits name, salary) and adds incentive.
# Constraint: Must use super()

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class SalesOfficer(Employee):
    def __init__(self, name, salary, incentive):
        # Use super() to call the Parent's __init__ method automatically
        super().__init__(name, salary)
        self.incentive = incentive

    def showTotalEarnings(self):
        total = self.salary + self.incentive
        print(f"Officer: {self.name}")
        print(f"Base Salary: {self.salary}")
        print(f"Incentive: {self.incentive}")
        print(f"Total Earnings: {total}")

# --- Testing the Code ---
print("\n--- Problem 3 Output ---")
officer = SalesOfficer("Bob", 50000, 5000)
officer.showTotalEarnings()
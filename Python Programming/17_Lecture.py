# 1. CREATE THE TEMPLATE (The Class)
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand    # Save the brand
        self.model = model    # Save the model
        self.year = year      # Save the year

    def display_info(self):
        # A simple function to print the car's details
        print(f"This car is a {self.year} {self.brand} {self.model}")

# 2. CREATE TWO CARS (The Objects)
# We use the template to make two different cars.
car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Honda", "Civic", 2010)

# 3. USE DOT NOTATION
# "Dot notation" just means using a dot (.) to get data out.

# Get specific data (Attribute)
print(car1.brand)   # Output: Toyota
print(car2.year)    # Output: 2010

# Use the car's function (Method)
car1.display_info() # Output: This car is a 2022 Toyota Camry
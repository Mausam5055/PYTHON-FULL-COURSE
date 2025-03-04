track = {"AB001": "Administrative", "AB002": "HUman Resource", "AB003": "IT", "AB004": "Sales"}

# 1. Add a new employee to the dictionary.
print(track)
track["AB005"] = "Electrical"
print(track)

# 2. Remove an employee from the dictionary
track.pop("AB003")
print(track)

# 3.  Find the department of a given employee ID
print(track["AB001"])

#  List all employees in a specific department.
specific_department = [emp for emp, dep in track.items() if dep == "Sales"]
print(specific_department)
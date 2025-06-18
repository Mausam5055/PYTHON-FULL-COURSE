# get(): It takes one to two arguments. While the first is the 
# key to search for, the second is the value to return if the key
#  isn’t found.

student = {"name": "Mausam", "age": 21}

# Safe access using get()
print(student.get("name"))          # Output: Mausam
print(student.get("course"))        # Output: None (no error)
print(student.get("course", "N/A")) # Output: N/A (default value)


#copy()
original = {"language": "Python", "level": "Intermediate"}
clone = original.copy()

print(clone)       # Output: {'language': 'Python', 'level': 'Intermediate'}
print(clone == original)   # True (same data)
print(clone is original)   # False (different memory locations)

#popitems()
profile = {"name": "Mausam", "age": 21, "country": "India"}
last_item = profile.popitem()

print(last_item)   # Output: ('country', 'India')
print(profile)     # Output: {'name': 'Mausam', 'age': 21}

#fromkeys:
keys = ['name', 'age', 'country']
default_dict = dict.fromkeys(keys, "Not available")

print(default_dict)
# Output: {'name': 'Not available', 'age': 'Not available', 'country': 'Not available'}



#update:
student = {"name": "Mausam", "age": 21}
new_data = {"age": 22, "course": "BTech"}

student.update(new_data)
print(student)
# Output: {'name': 'Mausam', 'age': 22, 'course': 'BTech'}

#Creating a Dictionary
x={"Name":"Mangal Singh", "Reg_no":"24BCE10599"} 
print(x)

#Accessing Dictionary Element - Using Key and not Position
print(x["Name"])

#Accessing Dictionary Element - Using Key and not Position
# print(x[0])    #will give KeyError as no such key is present




# Updating Dictionary
print(x)
x[1]="ONE" 
print(x)

# Add Element
x[3]="three"
print(x)

x[5]="four"
print(x)

#Checking whether an element is present or not using membership operator
print("Name" in x)

print(4 in x)

print(3 not in x)


# Copy - Dictionary is copied into another dictionary
print(x)
y=x.copy() 
print(y)

#Return a new view of the dictionary's items. It displays a list of dictionary’s (key, value) tuple pairs. 
print(x.items())

#displays list of keys in a dictionary
print(x.keys())

#displays list of values in dictionary
print(x.values())

#Remove the element with key and return its value from the dictionary
print("popped : ", x.pop(5))
print("popped : ", x.pop("Name"))
print(x)

# setdefault() - If key is in the dictionary, return its value. If key is not present, insert key with a value of dictionary and return dictionary
a={1:'ONE',2:'two'}
print(a)
a.setdefault(3,"three") 
print(a)

#It will add the dictionary with the existing dictionary
print(a)
b={4:"four"} 
a.update(b) 
print(a)

#It creates a dictionary from key and values
key={"apple","ball"} 
value="for kids" 
d=dict.fromkeys(key,value) 
print(d)

#length
print(a)
c=len(a)
print(c)

#clear()
print(a)
a.clear()
print(a)

# deleting the whole dictionary
a={1:"one",2:"two"} 
print(a)
del(a)
# print(a)    #a is deleted so it will give "NameError"


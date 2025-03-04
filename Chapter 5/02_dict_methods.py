# ---PROPERTIES OF PYTHON DICTIONARIES---

# 1. It is unordered.(ordere doesnt matter)
# 2. It is mutable.
# 3. It is indexed.
# 4. Cannot contain duplicate keys

# ----DICTIONARY METHODS---

# Consider the following dictionary.
# a={"name":"harry"
# "from":"india"
# "marks":[92,98,96]}

# • a.items(): Returns a list of (key,value)tuples.
# • a.keys(): Returns a list containing dictionary's keys.
# • a.update({"friends":}): Updates the dictionary with supplied 
# key-value pairs.
# • a.get("name"): Returns the value of the specified keys 
# (and value is returned EG.harry is returned here)

marks = {
    "Harry": 100,
    "Shubham": 56,
    "Rohan": 23,
    0: "Harry"
}

# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"Harry": 99, "Renuka": 100})
# print(marks)

print(marks.get("Mausam")) # Prints None
print(marks["Sauvik"]) # Returns an error

# --Dictionary is a collection of keys-value pairs.--

# Syntax: 
# a = {
# "key": "value",
# "harry": "code",
# "marks": "100",
# "list": [1, 2, 9]
# }
# print(a["key"]) # Output: "value"
# print(a["list"]) # Output: [1, 2, 9]

marks = {
    "Harry": 87,
    "Shubam" : 100,
    "Rohan": 56
}

print(marks,type(marks))

#here we printed the marks of all the sudents as well as the type of
#of datatype

#now if we want to get the mark of any particular student we
# cant simply write as,
#print(marks[0]): to get the mark of harry 
#rather we have to type print(marks["Harry"])

print(marks["Harry"])
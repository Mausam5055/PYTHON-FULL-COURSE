# ----LIST AND TUPLES----
#we can store different types ofd dtatypes inside a list as shown:

friends = ["Apple","Orange",5,360.06,"Rohan,","Akash"]

#now if we type: print(friends[0]) we will get output : "Apple"
print(friends[0])

#similarly if we had written: print(friends[2]) we would have 
#got an output : 5(i.e. the 3rd datatype from the above list)

#now if we want to change the list we can do so by changing anyone
#of the datatype from the list(lists are mutable but strings are not)

friends[0] = "Grapes" #we changed apple to grapes in the above list
print(friends[0])

#now after running the code we will get 1st apple and then a new output
#that we modified as grapes 

#it is also to be remembered that we cant do any such modification in case 
#strings since we already know that strings are immutable

#NOTES: 1. STRINGS ARE IMMUATABLE(EXISTING STRINGCANT BE MODIFIED )
#       2. LISTS ARE MUTUABLE(EXISTING LIST CAN BE MODIFIIED)

 #----SLIICING OF LIST_-----

print(friends[1:4])

#the above code: friends[1:4] will give us the value between 1 to 4
#from the list excluding 4 (i.e orange,5,360.4)
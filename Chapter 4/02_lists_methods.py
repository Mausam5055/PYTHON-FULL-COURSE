# -----------LIST METHODS.--------

# Consider the following list:
# l1 = [1,8,7,2,21,15]
# • l1.sort(): updates the list to [1,2,7,8,15,21]
# • l1.reverse(): updates the list to [15,21,2,7,8,1]
# • l1.append(8): adds 8 at the end of the list 
# • l1.insert(3,8): This will add 8 at 3 index
# • l1.pop(2): Will delete element at index 2 and return its value.
# • l1.remove(21): Will remove 21 from the list. 


friends = ["Apple","Orange",5,360.06,"Rohan,","Akash"]
friends.append("Harry")
print(friends)

#this above command adds a new name` "harry" to the list 
#i.e. the command completely modifies the list to a new list
#(this happnes because lists are mutable)

#but if we use any command to string it will not modify 
#the string rather it will change the string to a completely new string
#(this happens because strings are immutable)

#THE ABOVE DIFFERENCE BETWWEN STRING AND LIST IS VERY IMPORTRANT
#--see the string chapter and compare--
        #  1.string methods with 
        #  2. list methods
        #                for better understanding

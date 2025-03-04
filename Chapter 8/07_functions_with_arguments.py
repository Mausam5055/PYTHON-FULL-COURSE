# A function can also return value as shown below:

# def greet(name):
# gr = "hello"+ name
# return gr
# a = greet ("harry")

# # a will now contain "hello harry" 


def goodDay(name, ending):
    print("Good Day, " + name)
    print(ending)
    return "ok"   #we are saying the function to return its value 
                  #to 'a' (here a is being  below)

a = goodDay("Harry", "Thank you")  
print(a)

#if we dont use return " "  , then we will get printed "none" 
#after we run the code, 


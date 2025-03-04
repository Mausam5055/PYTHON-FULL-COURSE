def avg():
            a = int(input("Enter your number:"))  #all the three
            b = int(input("Enter your number:"))  #lines come inside
            c = int(input("Enter your number:"))  #the 'def(avg)function'

            average = (a+b+c)/3
            print(average)

     #now if we run the function like this nothing will happen 
     #we have to call out the function (means we have write 
     #'avg()'-- the number of times we want the average)
     #i,e if we want to take average 4 times we will write 
     # avg() function 
     # 4 times -- this is called "calling of a function"

avg()
avg()
avg()
avg()


   #note: inside  def(avg) function we have to put 5 
   # lines,since all these line of codes come under this
   #same def(avg) function,

   #all these 5 lines are to be put properly inside the def(avg)
   #function or else  we will get an error(see the format above)
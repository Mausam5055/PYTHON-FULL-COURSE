try:
    a = int(input("Hey,Enter a number:"))
    print(a)

except Exception as e:
    print(e)

  #now if we type anything except a number/integer as a input then
  # #our code will not crash like before  rather we will get an 
  # #invalid error writen the terminal in an organized way 
  #this happens bz of the try function
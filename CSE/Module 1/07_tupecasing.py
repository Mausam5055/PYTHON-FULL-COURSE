a = 2.5 #float
b = 5 #integer
print("sum1:", a+b) #output = 7.5 (i.e. float)

p = int(2.5) #typecasted float to integer
q = 5 
print("sum2:", p+q) #output = 7 (i.e. integer)

z=str(10) #10 is integer but inside str function i2t
          # got converted to a string when the output is generated
print(z)
print(type(z)) #10 = converted to string 

#Boolean : 1. zero means false 
       # 2. any non zero number represent true

print(bool(0))  # integer zero converted to boolean false 
print(bool(1)) #integer 1 converted to boolean true
#alternative method to convert integer to boolean by storing it as a 
#variable
print(bool(1+0j)) #in terms of vectors (j cap)
print(bool(0+0j)) #in terms of vectors (j cap)
t=bool(29) 
print(t)
print(type(t)) #intger converted to boolean clss typeS


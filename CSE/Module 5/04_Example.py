# add all numbers in an array
import array
array1 = array.array('i', [101, 210, 31, 49, 50])
sum=0
for i in array1:
    sum=sum+i
print(sum)


#add all odd numbers in an array
import array
array1 = array.array('i', [101, 210, 31, 49, 50])
sum=0
for x in array1:
    if(x % 2 !=0) :
        sum =sum+x
print(sum)
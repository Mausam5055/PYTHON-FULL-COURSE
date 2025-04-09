amstrong_numbers = []
for i in range(100,999): # intesd of i we can also write num 
   a = i//100
   b = (i//10)%10
   c = i%10
   if(a**3+b**3+c**3) == i:
    amstrong_numbers.append(i)
print(amstrong_numbers)
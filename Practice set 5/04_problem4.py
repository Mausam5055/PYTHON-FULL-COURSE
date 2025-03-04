# 4. What will be the length of following set s:
# s = set()
# s.add(20)
# s.add(20.0)
# s.add('20') # length of s after these operations?

s = set()
s.add(20)
s.add(20.0) #20 and 20.0 are same 
s.add('20') # length of s after these operations?

print(len(s))
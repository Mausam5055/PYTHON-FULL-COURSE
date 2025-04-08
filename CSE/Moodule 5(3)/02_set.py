s1 = {5,6,7,8,9,10}
s2 = set([5,6,7,8,9,10])
print(len(s1)) # 6
print(max(s1))
print(min(s1)) # 5
print(sum(s1)) # 45
print(sorted(s1)) # [5, 6, 7, 8, 9, 10]

print(s1.union(s2)) # {5, 6, 7, 8, 9, 10}
print(s1.intersection(s2)) # {5, 6, 7, 8, 9, 10}        
print(s1.difference(s2)) # set()
print(s1.issubset(s2)) # True
print(s1.issuperset(s2)) # True
print(s1.isdisjoint(s2)) # False
print(s1.pop()) # 5 (removes and returns an arbitrary element from the set)
print(s1) # {6, 7, 8, 9, 10}
print(s1.clear()) # None (removes all elements from the set)
print(s1) # set()                                                                                     
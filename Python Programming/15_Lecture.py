#various operations on Sets


A={1,2}
B={2,3,4,5}

print("A Set=",A)
print("B Set=",B)
print("lengthl of A=",len(A))
print("maximum of B:",max(B))
print("minimum of A:",min(A))
print("A union B =",A.union(B))
print("A intersection B=",A.intersection(B))
print("A difference B=",A.difference(B))
print("Asymmetric difference B=",A.symmetric_difference(B))
print("A is subset of B:",A.issubset(B))
print("A is superset of B:",A.issuperset(B)) 
print("After Adding new element 9 toset A:",A.add(9),A) 
print("After Deleting 4 from setB",B.remove(4),B)

c = A.union(B)
print("After Sorting:", sorted(c))
print("After Reversing:", sorted(c, reverse=True))
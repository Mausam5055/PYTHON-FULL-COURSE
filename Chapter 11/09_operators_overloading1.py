# --------OPERATOR OVERLOADING IN PYTHON --------

# Operators in Python can be overloaded using dunder methods.
# These methods are called when a given operator is used on the 
# objects.

# Operators in Python can be overloaded using the following methods:
# p1+p2 # p1.__add__(p2)
# p1-p2 # p1.__sub__(p2)
# p1*p2 # p1.__mul__(p2)
# p1/p2 # p1.__truediv__(p2)
# p1//p2 # p1.__floordiv__(p2)
# Other dunder/magic methods in Python:
# str__() # used to set what gets displayed upon calling str(obj)
# 45
# __len__() # used to set what gets displayed upon calling.__len__() or 
# len(obj)

class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, num):
        return self.n + num.n

n = Number(13)
m = Number(21)

print(n + m)


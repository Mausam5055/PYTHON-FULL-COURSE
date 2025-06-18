import numpy as np
def f(x):
    return np.cos(x)
def forward_difference(f, x, h=1e-5):
    return (f(x + h) - f(x)) / h
def backward_difference(f,x,h=1e-5):
    return (f(x) - f(x - h)) / h    
def central_difference(f,x,h=1e-5):
    return (f(x + h) - f(x - h)) / (2 * h)

fd_result = forward_difference(f, 0)#prints the forward difference at x=0
bd_result = backward_difference(f, 0)#prints the backward difference at x=0
cd_result = central_difference(f, 0)#prints the central difference at x=0

print("Forward Difference at x=0:", fd_result)
print("Backward Difference at x=0:", bd_result)
print("Central Difference at x=0:", cd_result)
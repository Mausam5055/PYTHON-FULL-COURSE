import math

def volume(l, b, h):
    return l * b * h

def surface_area(l, b, h):
    return 2 * (l * b + b * h + h * l)

def space_diagonal(l, b, h):
    return math.sqrt(l**2 + b**2 + h**2)

   
l = float(input("Enter the l of the cuboid: "))
b = float(input("Enter the b of the cuboid: "))
h = float(input("Enter the h of the cuboid: "))

volume = volume(l, b, h)
print(f"Volume of the cuboid: {volume} cubic units")

surface_area = surface_area(l, b, h)
print(f"Surface Area of the cuboid: {surface_area} square units")

space_diagonal = space_diagonal(l, b, h)
print(f"Space Diagonal of the cuboid: {space_diagonal} units")


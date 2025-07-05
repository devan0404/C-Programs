from math import pi

def tsa_cuboid(l,b,h):
    return 2 * (l * b + b * h + h * l)

def volume_cylinder(r, h):
    return round (pi * r**2 * h,2)

def volume_cube(a):
    return a**3
"""
Joe Donovan
jdonova9@uvm.edu
CS1210
"""


def sqrt(x):
    return x ** .5


def hypotenuse(a,b):
    x = (a**2) + (b**2)
    return sqrt(x)


def deg_reduce(x):
    return x % 360

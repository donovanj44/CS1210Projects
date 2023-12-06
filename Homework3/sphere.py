"""
Joe Donovan
jdonova9@uvm.edu
CS1210
"""

import math


def surface_area(radius):
    radius = float(radius)
    return 4 * math.pi * radius ** 2


def volume(radius):
    radius = float(radius)
    return (4 / 3) * math.pi * radius ** 3


radius = int(input("What is the radius of your sphere? "))
print(f"Surface area: {surface_area(radius):.2f}")
print(f"Volume: {volume(radius):.2f}")
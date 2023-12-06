"""
Joe Donovan
jdonova9@uvm.edu
CS1210
"""

import math

STREETS_PER_MILE = 20
AVENUES_PER_MILE = 7

streets_traveled = int(input("How many street blocks do you need to travel? ")) / 20
avenues_traveled = int(input("How many avenue blocks do you need to travel? ")) / 7


def taxicab_distance(streets, avenues):
    return streets + avenues


def crow_distance(streets, avenues):
    return hypotenuse(streets, avenues)


def hypotenuse(a, b):
    x = (a ** 2) + (b ** 2)
    return math.sqrt(x)


print(f"The crows flight is {taxicab_distance(streets_traveled, avenues_traveled) - crow_distance(streets_traveled, avenues_traveled):.2f} miles shorter")

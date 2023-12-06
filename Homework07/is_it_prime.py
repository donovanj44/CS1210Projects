"""
Joe Donovan
jdonova9@uvm.edu
CS1210
"""

import math


def prime_test(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return f"{n} is not prime."
    return f"{n} is prime"


if __name__ == "__main__":
    num = 0
    while num < 2:
        num = int(input("Enter an integer > 1: "))
    print(prime_test(num))

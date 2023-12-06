"""
Joe Donovan
jdonova9@uvm.edu
CS1210
"""


def quotient(r, s):
    count = 0
    while r - s >= 0:
        r = r - s
        count = count + 1
    return count


def remainder(r, s):
    while r - s >= 0:
        r = r - s
    return r


if __name__ == "__main__":
    dividend = 0
    while dividend <= 0 :
        dividend = int(input("Enter the dividend (a positive integer): "))
    divisor = 0
    while divisor <= 0:
        divisor = int(input("Enter the divisor (a positive integer): "))
    print(f"{dividend} // {divisor} = {quotient(dividend, divisor)}")
    print(f"{dividend} % {divisor} = {remainder(dividend, divisor)}")

"""
Joe Donovan
jdonova9@uvm.edu
CS1210
"""


def f_to_c(f):
    return (f - 32) * (5 / 9)


temp = float(input("Enter temperature in degrees F: "))

print(f'{"Fahrenheit    ":0<}'
      f'{"Celsius":6>}')
print(f'{temp - 10:>10,.1f}'
      f'{f_to_c(temp - 10):>11,.1f}')
print(f'{temp:>10,.1f}'
      f'{f_to_c(temp):>11,.1f}')
print(f'{temp + 10:>10,.1f}'
      f'{f_to_c(temp + 10):>11,.1f}')

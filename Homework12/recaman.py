"""
Joe Donovan
jdonova9@uvm.edu
CS1210
"""


def next_recaman(lst):
    if not lst:
        return 0
    if lst[-1] - len(lst) > 0 and lst[-1] - len(lst) not in lst:
        return lst[-1] - len(lst)
    else:
        return lst[-1] + len(lst)

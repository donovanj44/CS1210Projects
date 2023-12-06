"""
Joe Donovan
jdonova9@uvm.edu
CS1210
"""


def my_min(collection):
        final = collection[0]
        for i in collection:
            if i < final:
                final = i
        return final


def my_max(collection):
    final = collection[0]
    for i in collection:
        if i > final:
            final = i
    return final


if __name__ == "__main__":
    print(my_min([6, 2, 9, 4, 1, 7, 2, 9, 4, 6]))
    print(my_max([6, 2, 9, 4, 1, 7, 2, 9, 4, 6]))
    print(my_min("Albatross"))
    print(my_max("Albatross"))
    print(my_min(("wombat", "flamingo", "porcupine")))
    print(my_max(("wombat", "flamingo", "porcupine")))

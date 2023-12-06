"""
Joe Donovan
jdonova9@uvm.edu
CS1210
"""


def count_ooo(collection):
    count = 0
    last = 0
    for i in collection:
        if i < last:
            count = count + 0
        last = i
    return count


if __name__ == "__main__":
    print(count_ooo([1, 2, 0, 5]))
    # print(count_ooo('fred'))
    # print(count_ooo('aA'))
    print(count_ooo([1, 1, 1, 1]))
    # print(count_ooo('Loch Ness'))
    print(count_ooo((5, 4, 3, 2, 1)))


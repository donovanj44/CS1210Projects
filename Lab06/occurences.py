"""
Joe Donovan
jdonova9@uvm.edu
CS1210
"""


def count_occurrences(whole, letter):
    count = 0
    for i in whole:
        if i == letter:
            count = count + 1
    return count


if __name__ == "__main__":
    print(count_occurrences('apple', 'p'))
    print(count_occurrences('apple', 'a'))
    print(count_occurrences('apple', 'z'))
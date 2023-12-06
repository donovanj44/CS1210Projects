"""
Joe Donovan
jdonova9@uvm.edu
CS1210
"""


if __name__ == "__main__":
    stack = []
    word = input("Enter a string, and I'll print it backwards! ")
    for i, e in enumerate(word):
        stack.append(e)
    while stack:
        print(stack.pop(), end='')
    print()

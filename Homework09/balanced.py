"""
Joe Donovan
jdonova9@uvm.edu
CS1210
"""


def balanced(s):
    stack = []

    for i in s:
        if i == '(':
            stack.append(i)
        if i == ')' and stack:
            stack.pop()
        elif i == ')' and not stack:
            return False
    return len(stack) == 0

if __name__ == "__main__":
    testString = input("Enter a string containing parentheses: ")
    if balanced(testString):
        print("Parentheses are balanced!")
    elif not balanced(testString):
        print("Parentheses are not balanced!")

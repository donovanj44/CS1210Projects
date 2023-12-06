"""
Joe Donovan
jdonova9@uvm.edu
CS1210
"""


if __name__ == "__main__":
    num = int(input("Enter an integer greater than 1: "))
    list = []
    while num >= 1:
        if num % 2 == 0:
            num = num // 2
            list.append(num)
        else:
            num = 3 * num + 1
            list.append(num)
    print(f"{list}")
    print(f"The length of the sequence is {len(list) + 1}")
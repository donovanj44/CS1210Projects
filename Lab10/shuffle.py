import random


def shuffle(lst):
    new_lst = []
    while lst:
        new_lst.append(random.choice(lst))
        lst.remove(new_lst[-1])
    return new_lst


if __name__ == "__main__":
    lst_length = 0
    original_lst = []
    while lst_length <= 5:
        try:
            lst_length = int(input("How many elements in your list (n > 5)? "))
        except ValueError:
            print("Unable to convert input to integer")
    for x in range(lst_length):
        original_lst.append(input(f"Enter item at index {x}: "))
    copy_lst = original_lst.copy()
    print(shuffle(copy_lst))
    print(original_lst)


import random

if __name__ == "__main__":
    count = 0
    money = int(input("How much money does the gambler start with: "))
    while money > 0:
        flip = random.randint(0, 1)
        call = random.randint(0,1)
        if flip == call:
            money = money + 1
        else:
            money = money - 1
        count = count + 1
    print(f"Ran out of money in {count} flips")

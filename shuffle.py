import random

if __name__ == "__main__":
    cards = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']
    random.shuffle(cards)
    print(f"{cards}")
    while cards:
        print(f"{cards[0]}")
        cards.pop(0)

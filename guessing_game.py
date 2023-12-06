import random


if __name__ == "__main__":
    print("Guessing Game \nHigher or Lower from 1-100\n10 Tries")
    guess = 0
    answer = random.randint(1, 100)
    print(f"Answer is {answer}")
    for i in range(10):
        guess = int(input("Guess a number: "))
        if guess == answer:
            print(f"You win! Number was: {answer}")
            break
        elif guess > answer:
            print(f"{guess} is too high")
        elif guess < answer:
            print(f"{guess} is too low")
        if i == 9:
            print(f"You lose! Number was {answer}")

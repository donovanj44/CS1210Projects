import random


WIN_GRID = [[0, 1, -1],
            [-1, 0, 1],
            [1, -1, 0]]
LABELS = ['rock', 'paper', 'scissors']


if __name__ == "__main__":
    while True:
        computerChoice = random.randint(0,2)
        choice = int(input("What's your choice? 0) rock, 1) paper, 2) scissors? or 4) quit: "))
        if WIN_GRID[computerChoice][choice] == -1:
            print(f"You: {LABELS[choice]}, me: {LABELS[computerChoice]}")
            print(f"You lose!")
        elif WIN_GRID[computerChoice][choice] == 0:
            print(f"You: {LABELS[choice]}, me: {LABELS[computerChoice]}")
            print(f"Draw!")
        elif WIN_GRID[computerChoice][choice] == 2:
            print(f"You: {LABELS[choice]}, me: {LABELS[computerChoice]}")
            print(f"You win!")
        elif choice == 4:
            print(f"Goodbye")
            break

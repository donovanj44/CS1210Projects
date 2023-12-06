"""
Joe Donovan
jdonova9@uvm.edu
CS1210
"""


def mean(calories):
    return float(sum(calories) / len(calories))


if __name__ == "__main__":
    calories = [int(input("How many calories did you eat at breakfast? "))]
    print(f"You have now consumed {sum(calories):,} calories from 1 meal")
    calories.append(int(input("How many calories did you eat"
                              " at your mid-morning snack? ")))
    print(f"You have now consumed {sum(calories):,} calories from 2 meals")
    calories.append(int(input("How many calories did you eat at lunch? ")))
    print(f"You have now consumed {sum(calories):,} calories from 3 meals")
    calories.append(int(input("How many calories did you eat at dinner? ")))
    print(f"You have now consumed {sum(calories):,}"
          f" calories from 4 meals")
    calories.append(int(input("How many calories "
                              "did you eat at your evening snack? ")))
    print(f"Total calories consumed: {sum(calories):,}")
    print(f""f"Average calories per meal or snack: {mean(calories):.1f}")

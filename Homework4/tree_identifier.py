"""
Joe Donovan
jdonova9@uvm.edu
CS1210
"""


if __name__ == "__main__":
    choice = input("Leaves (l) or needles (n)? ").lower()

    if choice == "l":
        choice = input("Simple (s) or compound (c)? ").lower()
        if choice == "s":
            print("Maple")
        elif choice == "c":
            print("Ash")
        else:
            print("Invalid choice")
    elif choice == "n":
        choice = input("Individual (i) or clustered (c)? ").lower()
        if choice == "i":
            print("Spruce")
        elif choice == "c":
            print("Pine")
        else:
            print("Invalid choice")
    else:
        print("Invalid choice")

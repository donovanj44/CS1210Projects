"""
Joe Donovan
jdonova9@uvm.edu
CS1210
"""

if __name__ == "__main__":
    filename = input("Enter the name of the file to read: ")
    while True:
        if filename == "q":
            exit(0)
        try:
            with open(filename, "r") as fh:
                print(fh.read())
                fh.close()
                break
        except FileNotFoundError:
            print("Could not find file")
            filename = input("Enter the name of the file to read,"
                             " or type q to exit: ")

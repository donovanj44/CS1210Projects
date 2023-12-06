integer = int(input("Enter an integer: "))

if integer < 0:
    print(f"The least significant digit is {((integer * -1) % 10) * -1} ")
else:
    print(f"The least significant digit is {integer % 100}")

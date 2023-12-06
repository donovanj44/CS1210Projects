integer = int(input("Enter a positive integer: "))
if integer < 0:
    print(f"{integer} is not positive!")
else:
    print(f"The least significant digit is {integer % 10}")
num1 = int(input("Enter the integer for row 0, column 0: "))
num2 = int(input("Enter the integer for row 0, column 1: "))
num3 = int(input("Enter the integer for row 1, column 0: "))
num4 = int(input("Enter the integer for row 1, column 1: "))
array = [[num1, num2], [num3, num4]]
print(f"The 2x2 list is {array}")
print(f"The sums of the columns are {array[0][0] + array[1][0]} and"
      f" {array[0][1] + array[1][1]}")

from num_to_digits import num_to_digits

userNum = int(input("Enter a number from 0-999: "))
print(f"Max digit: {num_to_digits(userNum)[0]}; min digit: {num_to_digits(userNum)[-1]}"
      f"; sum: {sum(num_to_digits(userNum))}")

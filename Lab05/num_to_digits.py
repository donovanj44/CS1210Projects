def num_to_digits(num):
    array = [(num % 1000) // 100, (num % 100) // 10, num % 10]
    array.sort(reverse=True)
    digits = (array[0], array[1], array[2])
    return digits


if __name__ == "__main__":
    userNum = int(input("Enter a number from 0-999: "))
    print(f"Max digit: {num_to_digits(userNum)[0]}; min digit: {num_to_digits(userNum)[-1]}")
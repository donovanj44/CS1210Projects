"""
Joe Donovan
jdonova9@uvm.edu
CS1210
"""


def std_dev(numbers):
    mean = sum(numbers) / len(numbers)
    return (sum([((x - mean) ** 2) for x in numbers]) / len(numbers)) ** 0.5


if __name__ == "__main__":
    numbers = []
    for i in range(5):
        numbers.append((float(input("Enter a real number: "))))
    mean = sum(numbers) / len(numbers)
    print(f"The mean is {mean:.3f} and the standard deviation is {std_dev(numbers):.3f}")

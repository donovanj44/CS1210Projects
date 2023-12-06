"""
Joe Donovan
jdonova9@uvm.edu
CS1210
"""

import csv


def mean(lst):
    return sum(lst) / len(lst)


def std_dev(lst):
    avg = mean(lst)
    return (sum([((x - avg) ** 2) for x in lst]) / len(lst)) ** 0.5


if __name__ == "__main__":
    with open("co2_ppm.csv", "r") as fr:
        reader = csv.reader(fr)
        ppmList = [float(row[1]) for row in reader]
    fr.close()
    print(ppmList)
    stdDev = std_dev(ppmList)
    with open("results.txt", "w") as fw:
        fw.write(f"Mean: {mean(ppmList):.2f} \n"
                 f"Standard Deviation: {std_dev(ppmList):.2f} \n"
                 f"Most recent observation: {ppmList[-1]:.2f} \n")
    fw.close()

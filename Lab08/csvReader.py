import csv


with open("scratch.csv", 'r') as file:
    total = 0
    for row in csv.reader(file):
        total = total + float(row[2])
    file.close()
print(total)
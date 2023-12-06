import csv
import matplotlib.pyplot as plt


if __name__ == "__main__":
    x_players = []
    y_hrs = []
    with open("sluggers.csv", newline="") as fh:
        reader = csv.reader(fh)
        next(reader)
        for row in reader:
            x_players.append(row[0])
            y_hrs.append(float(row[1]))
    plt.title("Sluggers")
    plt.ylabel("Home Runs")
    plt.xlabel("Players")
    plt.bar(x_players, y_hrs, 0.5, color = "blue")
    plt.show()

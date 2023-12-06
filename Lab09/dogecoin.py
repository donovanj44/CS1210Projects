import csv
import matplotlib.pyplot as plt


if __name__ == "__main__":
    x_dates = []
    y_closing = []
    with open("dogecoin_history.csv", newline="") as fh:
        reader = csv.reader(fh)
        next(reader)
        for row in reader:
            x_dates.append(row[0])
            y_closing.append(float(row[4]))
    plt.title("DOGE")
    plt.ylabel("Closing price (USD)")
    plt.xlabel("Date")
    plt.xticks(rotation=60)
    plt.plot(x_dates, y_closing)
    plt.show()
    print(x_dates)
    print(y_closing)

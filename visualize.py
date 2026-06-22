import csv
import json
import matplotlib.pyplot as plt


def load_data(filename):
    mileages = []
    prices = []

    with open(filename, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            mileages.append(float(row["km"]))
            prices.append(float(row["price"]))

    return mileages, prices


def load_model(filename):
    with open(filename, "r") as file:
        model = json.load(file)

    return model


def normalize_value(value, min_value, max_value):
    if max_value == min_value:
        return 0
    return (value - min_value) / (max_value - min_value)


def estimate_price(mileage, theta0, theta1):
    return theta0 + theta1 * mileage


def main():
    try:
        mileages, prices = load_data("data.csv")
        model = load_model("model.json")
    except FileNotFoundError as error:
        print("Error:", error)
        print("Please make sure data.csv and model.json exist.")
        return

    theta0 = model["theta0"]
    theta1 = model["theta1"]
    min_mileage = model["min_mileage"]
    max_mileage = model["max_mileage"]

    line_x = [min_mileage, max_mileage]

    line_y = []

    for mileage in line_x:
        normalized_mileage = normalize_value(mileage, min_mileage, max_mileage)
        predicted_price = estimate_price(normalized_mileage, theta0, theta1)
        line_y.append(predicted_price)

    plt.scatter(mileages, prices, label="Real data")
    plt.plot(line_x, line_y, label="Linear regression line")

    plt.xlabel("Mileage")
    plt.ylabel("Price")
    plt.title("Car Price Prediction with Linear Regression")

    plt.legend()
    plt.grid(True)

    plt.legend()
    plt.grid(True)

    plt.savefig("linear_regression.png", dpi=300, bbox_inches="tight")
    print("Graph saved to linear_regression.png")


if __name__ == "__main__":
    main()
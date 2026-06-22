import csv
import json
import math


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


def calculate_metrics(mileages, prices, model):
    theta0 = model["theta0"]
    theta1 = model["theta1"]
    min_mileage = model["min_mileage"]
    max_mileage = model["max_mileage"]

    total_absolute_error = 0.0
    total_squared_error = 0.0
    total_absolute_percentage_error = 0.0

    mean_price = sum(prices) / len(prices)

    ss_res = 0.0
    ss_tot = 0.0

    m = len(mileages)

    for i in range(m):
        normalized_mileage = normalize_value(
            mileages[i],
            min_mileage,
            max_mileage
        )

        prediction = estimate_price(normalized_mileage, theta0, theta1)
        error = prediction - prices[i]

        total_absolute_error += abs(error)
        total_squared_error += error ** 2

        if prices[i] != 0:
            total_absolute_percentage_error += abs(error / prices[i])

        ss_res += (prices[i] - prediction) ** 2
        ss_tot += (prices[i] - mean_price) ** 2

    mae = total_absolute_error / m
    mse = total_squared_error / m
    rmse = math.sqrt(mse)

    if ss_tot == 0:
        r2_score = 0
    else:
        r2_score = 1 - (ss_res / ss_tot)

    mape = (total_absolute_percentage_error / m) * 100
    approximate_precision = 100 - mape

    return mae, mse, rmse, r2_score, mape, approximate_precision


def main():
    try:
        mileages, prices = load_data("data.csv")
        model = load_model("model.json")
    except FileNotFoundError as error:
        print("Error:", error)
        print("Please make sure data.csv and model.json exist.")
        return

    mae, mse, rmse, r2_score, mape, approximate_precision = calculate_metrics(
        mileages,
        prices,
        model
    )

    print("Model evaluation results")
    print("------------------------")
    print(f"MAE: {mae:.2f}")
    print(f"MSE: {mse:.2f}")
    print(f"RMSE: {rmse:.2f}")
    print(f"R2 score: {r2_score:.4f}")
    print(f"MAPE: {mape:.2f}%")
    print(f"Approximate precision: {approximate_precision:.2f}%")


if __name__ == "__main__":
    main()
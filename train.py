import csv
import json

def load_data(filename):
    mileages = []
    prices = []

    with open(filename, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            mileages.append(float(row["km"]))
            prices.append(float(row["price"]))

    return mileages, prices

def estimate_price(mileage, theta0, theta1):
    return theta0 + theta1 * mileage

def calculate_error(prediction, real_price):
    return prediction - real_price

def calculate_mse(mileages, prices, theta0, theta1):
    total_error = 0
    m = len(mileages)

    for i in range(m):
        prediction = estimate_price(mileages[i], theta0, theta1)
        error = prediction - prices[i]
        total_error += error ** 2

    return total_error / m

def normalize_value(value, min_value, max_value):
    if max_value == min_value:
        return 0
    return (value - min_value) / (max_value - min_value)


def normalize_mileages(mileages):
    min_mileage = min(mileages)
    max_mileage = max(mileages)

    normalized_mileages = []

    for mileage in mileages:
        normalized = normalize_value(mileage, min_mileage, max_mileage)
        normalized_mileages.append(normalized)

    return normalized_mileages, min_mileage, max_mileage

def train_model(mileages, prices, learning_rate, iterations):
    theta0 = 0.0
    theta1 = 0.0

    m = len(mileages)

    for iteration in range(iterations):
        sum_theta0 = 0.0
        sum_theta1 = 0.0

        for i in range(m):
            prediction = estimate_price(mileages[i], theta0, theta1)
            error = prediction - prices[i]

            sum_theta0 += error
            sum_theta1 += error * mileages[i]

        tmp_theta0 = learning_rate * (sum_theta0 / m)
        tmp_theta1 = learning_rate * (sum_theta1 / m)

        theta0 = theta0 - tmp_theta0
        theta1 = theta1 - tmp_theta1

    return theta0, theta1

def save_model(filename, theta0, theta1, min_mileage, max_mileage):
    model = {
        "theta0": theta0,
        "theta1": theta1,
        "min_mileage": min_mileage,
        "max_mileage": max_mileage
    }

    with open(filename, "w") as file:
        json.dump(model, file, indent=4)

def main():
    mileages, prices = load_data("data.csv")

    normalized_mileages, min_mileage, max_mileage = normalize_mileages(mileages)

    theta0 = 0.0
    theta1 = 0.0

    initial_mse = calculate_mse(normalized_mileages, prices, theta0, theta1)

    learning_rate = 0.1
    iterations = 10000

    theta0, theta1 = train_model(
        normalized_mileages,
        prices,
        learning_rate,
        iterations
    )

    final_mse = calculate_mse(normalized_mileages, prices, theta0, theta1)

    save_model("model.json", theta0, theta1, min_mileage, max_mileage)

    first_mileage = mileages[0]
    first_normalized_mileage = normalize_value(first_mileage, min_mileage, max_mileage)
    first_real_price = prices[0]
    first_prediction = estimate_price(first_normalized_mileage, theta0, theta1)

    print("Data loaded successfully.")
    print("Total rows:", len(mileages))

    print("Min mileage:", min_mileage)
    print("Max mileage:", max_mileage)

    print("Initial MSE:", initial_mse)
    print("Final MSE:", final_mse)

    print("Theta0:", theta0)
    print("Theta1:", theta1)

    print("Model saved to model.json")

    print("First mileage:", first_mileage)
    print("First real price:", first_real_price)
    print("First prediction after training:", first_prediction)

if __name__ == "__main__":
    main()
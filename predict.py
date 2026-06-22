import json


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
        model = load_model("model.json")
    except FileNotFoundError:
        print("Error: model.json not found.")
        print("Please run train.py before using predict.py.")
        return

    theta0 = model["theta0"]
    theta1 = model["theta1"]
    min_mileage = model["min_mileage"]
    max_mileage = model["max_mileage"]

    user_input = input("Enter mileage: ")

    try:
        mileage = float(user_input)
    except ValueError:
        print("Error: mileage must be a number.")
        return

    if mileage < 0:
        print("Error: mileage cannot be negative.")
        return

    if mileage < min_mileage or mileage > max_mileage:
        print("Warning: this mileage is outside the training data range.")
        print("Training range:", min_mileage, "-", max_mileage)
        print("The prediction may not be reliable.")

    normalized_mileage = normalize_value(mileage, min_mileage, max_mileage)

    estimated_price = estimate_price(normalized_mileage, theta0, theta1)

    print(f"Estimated price: {estimated_price:.2f}")

    if estimated_price < 0:
        print("Warning: the estimated price is negative.")
        print("This usually means the input is too far outside the training data range.")


if __name__ == "__main__":
    main()